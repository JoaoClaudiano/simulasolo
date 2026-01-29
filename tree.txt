simula_solo/
│
├── core/                         # 🧠 NÚCLEO GEOTÉCNICO (SEM UI)
│   ├── soil/
│   │   ├── stress_state.py       # Tensões, σ1, σ3, Mohr
│   │   ├── mohr_coulomb.py
│   │   ├── stress_path.py
│   │   └── transformations.py
│   │
│   ├── shallow_foundations/
│   │   ├── boussinesq.py
│   │   ├── terzaghi.py
│   │   ├── bearing_capacity.py
│   │   ├── settlements.py
│   │   └── interaction_diagram.py
│   │
│   ├── deep_foundations/
│   │   ├── aoki_velloso.py
│   │   ├── decourt_quaresma.py
│   │   ├── pile_capacity.py
│   │   ├── pile_settlement.py
│   │   └── group_effect.py
│   │
│   ├── slope_stability/          # 🔄 expansão futura
│   ├── earth_pressure/
│   ├── consolidation/
│   └── fem/
│
├── norms/                        # 📐 NORMAS TÉCNICAS
│   ├── nbr_6122.py
│   ├── nbr_6118.py
│   └── checks.py
│
├── services/                     # 🔌 API INTERNA
│   ├── soil_service.py
│   ├── shallow_service.py
│   ├── deep_service.py
│   └── report_service.py
│
├── exports/                      # 📤 EXPORTAÇÃO
│   ├── export_csv.py
│   ├── export_excel.py
│   ├── export_pdf.py
│   ├── export_html.py
│   └── export_json.py
│
├── visualization/                # 📊 GRÁFICOS
│   ├── mohr_plot.py
│   ├── stress_3d.py
│   ├── soil_profile.py
│   ├── interaction_plot.py
│   └── contour_plots.py
│
├── data/
│   ├── soil_database.json
│   ├── spt_samples.csv
│   └── units.yaml
│
├── app/                          # 🖥️ FRONTEND (STREAMLIT)
│   ├── pages/
│   │   ├── 1_solo_e_tensoes.py
│   │   ├── 2_sapatas.py
│   │   ├── 3_estacas.py
│   │   ├── 4_visualizacoes.py
│   │   ├── 5_relatorios.py
│   │   └── 6_configuracoes.py
│   │
│   ├── components/
│   │   ├── sidebar.py
│   │   ├── unit_selector.py
│   │   └── soil_selector.py
│   │
│   └── app.py
│
├── tests/
│   ├── test_soil.py
│   ├── test_shallow.py
│   ├── test_deep.py
│   └── test_norms.py
│
├── docs/
│   ├── metodologia.md
│   ├── fundamentos_teoricos.md
│   └── arquitetura.md
│
└── README.md
