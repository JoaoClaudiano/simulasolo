import os
import re
import shutil

# 📂 Configurações
ROOT_DIR = "./"  # raiz do projeto
BACKUP_DIR = "./backup_before_indent_fix"

# 🔹 Criar backup completo
if not os.path.exists(BACKUP_DIR):
    shutil.copytree(ROOT_DIR, BACKUP_DIR, ignore=shutil.ignore_patterns('backup_before_indent_fix', '.git', '__pycache__', '*.pyc'))
    print(f"[✔] Backup criado em: {BACKUP_DIR}")
else:
    print(f"[ℹ] Backup já existe: {BACKUP_DIR}")

# 🔹 Regex
CLASS_REGEX = re.compile(r"^(class\s+\w+.*?):\s*(#.*)?$")
DECORATOR_REGEX = re.compile(r"^\s*@\w+")
DEF_REGEX = re.compile(r"^\s*def\s+\w+\(.*\)\s*:")
ELIF_ELSE_REGEX = re.compile(r"^\s*(elif|else)[\s:]")

def indent_line(line, level=1):
    return (" " * 4 * level) + line.lstrip()

def needs_indented_block(line):
    """Check if line needs an indented block after it"""
    stripped = line.strip()
    if not stripped:
        return False
    # Check if line ends with : (but not inside a string)
    # Simple check: ends with : or :\s*#comment
    if re.search(r':\s*(#.*)?$', stripped):
        return True
    return False

def fix_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    fixed_lines = []
    i = 0
    n = len(lines)
    
    def process_block(start_i, base_indent):
        """Process a block of code and return the fixed lines and next index"""
        nonlocal i
        i = start_i
        result = []
        
        while i < n:
            line = lines[i]
            stripped = line.lstrip()
            
            # Empty lines
            if stripped == "":
                result.append("\n")
                i += 1
                continue
            
            # Check if this is a new class definition (end of current block)
            if CLASS_REGEX.match(stripped):
                break
            
            # Check if this could be a class-level item when we're in a method
            if base_indent > 1:  # We're in a method body
                # Check for decorator or def at class level
                if DECORATOR_REGEX.match(stripped) or DEF_REGEX.match(stripped):
                    break
            
            # Check for elif/else - they should be at the parent level, not nested
            if ELIF_ELSE_REGEX.match(stripped) and base_indent > 0:
                # This elif/else belongs to the parent level
                break
            
            # Add the line with current indentation
            result.append(indent_line(line, level=base_indent))
            i += 1
            
            # Check if this line needs an indented block after it
            if needs_indented_block(line):
                # Recursively process the nested block
                nested_result, i = process_block(i, base_indent + 1)
                result.extend(nested_result)
                
                # After processing nested block, check for elif/else
                while i < n:
                    next_line = lines[i]
                    next_stripped = next_line.lstrip()
                    
                    if ELIF_ELSE_REGEX.match(next_stripped):
                        # Add elif/else at same level as the original if
                        result.append(indent_line(next_line, level=base_indent))
                        i += 1
                        
                        # Process the elif/else block
                        elif_else_result, i = process_block(i, base_indent + 1)
                        result.extend(elif_else_result)
                    else:
                        break
        
        return result, i
    
    while i < n:
        line = lines[i]
        class_match = CLASS_REGEX.match(line)
        
        if class_match:
            # Add the class line
            fixed_lines.append(line.rstrip() + "\n")
            i += 1

            # Track if class has content
            class_has_content = False
            
            # Process class body
            while i < n:
                current = lines[i]
                stripped = current.lstrip()

                # End of class: new class detected
                if CLASS_REGEX.match(stripped):
                    break

                # Empty lines
                if stripped == "":
                    fixed_lines.append("\n")
                    i += 1
                    continue

                # Decorators at class level
                if DECORATOR_REGEX.match(stripped):
                    fixed_lines.append(indent_line(stripped, level=1))
                    class_has_content = True
                    i += 1
                    continue

                # Methods at class level - but be careful, already indented defs stay as-is
                if DEF_REGEX.match(stripped):
                    fixed_lines.append(indent_line(stripped, level=1))
                    class_has_content = True
                    i += 1
                    # Process method body
                    method_body, i = process_block(i, base_indent=2)
                    fixed_lines.extend(method_body)
                    continue

                # Class attributes or other content
                fixed_lines.append(indent_line(stripped, level=1))
                class_has_content = True
                i += 1

            # If class is empty, add pass
            if not class_has_content:
                fixed_lines.append("    pass\n")
            continue

        # Line outside of class - keep original
        fixed_lines.append(line)
        i += 1

    with open(filepath, "w", encoding="utf-8") as f:
        f.writelines(fixed_lines)
    print(f"[✔] Corrigido: {filepath}")

# 🔹 Percorrer todo o projeto
for root, dirs, files in os.walk(ROOT_DIR):
    if BACKUP_DIR in root:
        continue
    for file in files:
        if file.endswith(".py"):
            fix_file(os.path.join(root, file))

print("\n[✅] Todos os arquivos Python processados com sucesso.")
