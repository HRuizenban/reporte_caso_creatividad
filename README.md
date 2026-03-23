# Creatividad digital programacion
Columnas disponibles:
Index(['id_campana', 'fecha', 'cliente', 'plataforma', 'formato',
       'duracion_seg', 'objetivo', 'pais', 'presupuesto_usd', 'costo_usd',
       'impresiones', 'alcance', 'clicks', 'reproducciones_3s',
       'reproducciones_100', 'conversiones', 'ingresos_usd',
       'calificacion_creativa'],
      dtype='str')

Primeros datos con métricas:
  id_campana       fecha     cliente plataforma      formato  duracion_seg  ... conversiones ingresos_usd  calificacion_creativa       ctr       cvr       roi
0  CAMP-0001  2025-01-02     LumaAds    YouTube         Reel            30  ...           82       626.92                     79  0.012742  0.020133 -0.734000
1  CAMP-0002  2025-01-03  FrameHouse   Facebook         Reel            25  ...           93       678.65                     93  0.019998  0.025013 -0.188606
2  CAMP-0003  2025-01-04  PixelForge   Facebook  Video Largo            60  ...           24      1082.33                     63  0.009704  0.049180  2.717814
3  CAMP-0004  2025-01-05  FrameHouse    YouTube  Video Largo            90  ...           19        64.42                     69  0.008922  0.007627 -0.950621
4  CAMP-0005  2025-01-06   NeoStudio  Instagram  Video Largo            45  ...          137      5787.29                     73  0.013333  0.072950  8.028815

[5 rows x 21 columns]

--- RESUMEN GENERAL ---
Total campañas: 180
Costo total: 279370.66
Ingresos totales: 1242557.17
ROI promedio: 3.5

CTR promedio por formato:
formato
Reel           0.020697
Story          0.018089
Carrusel       0.016975
Imagen         0.013379
Video Largo    0.013289

ROI promedio por plataforma:
plataforma
TikTok       6.672855
Instagram    3.146111
Facebook     2.167606
YouTube      1.974836
X            1.769305

Outliers detectados en CTR: 3

--- TOP 5 CAMPAÑAS POR ROI ---
id_campana plataforma  formato       roi
 CAMP-0151     TikTok    Story 33.427567
 CAMP-0055     TikTok    Story 29.794451
 CAMP-0159     TikTok     Reel 27.994398
 CAMP-0101     TikTok Carrusel 27.176850
 CAMP-0067     TikTok     Reel 23.848913

--- BOTTOM 5 CAMPAÑAS POR ROI ---
id_campana plataforma     formato       roi
 CAMP-0004    YouTube Video Largo -0.950621
 CAMP-0142    YouTube       Story -0.948554
 CAMP-0145  Instagram      Imagen -0.934886
 CAMP-0014    YouTube        Reel -0.934301
 CAMP-0015          X        Reel -0.928064

<img width="644" height="557" alt="image" src="https://github.com/user-attachments/assets/4fd050dd-99c9-4260-aa8a-65fb5896e573" />

<img width="644" height="554" alt="image" src="https://github.com/user-attachments/assets/a9c75bfe-6e73-4762-8cc7-8f224a8bceea" />


