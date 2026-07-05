import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from IPython.display import display, HTML

# 1. Configuración de Estética Neon Dark
neon_css = """
<style>
    :root {
        --bg-color: #0d1117;
        --neon-cyan: #00f3ff;
        --neon-magenta: #ff00ff;
        --neon-lime: #39ff14;
        --text-color: #e6edf3;
        --card-bg: #161b22;
    }
    
    body {
        background-color: var(--bg-color) !important;
        color: var(--text-color) !important;
    }
    
    .neon-card {
        background-color: var(--card-bg);
        border: 1px solid var(--neon-cyan);
        box-shadow: 0 0 10px var(--neon-cyan);
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
        transition: transform 0.3s ease;
    }
    
    .neon-card:hover {
        transform: scale(1.02);
        box-shadow: 0 0 20px var(--neon-magenta);
        border-color: var(--neon-magenta);
    }
    
    .neon-title {
        color: var(--neon-cyan);
        text-shadow: 0 0 5px var(--neon-cyan);
        font-family: 'Courier New', Courier, monospace;
        font-weight: bold;
    }
    
    .neon-metric {
        font-size: 2em;
        color: var(--neon-lime);
        text-shadow: 0 0 5px var(--neon-lime);
    }
    
    /* Animación de entrada */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .animate-in {
        animation: fadeIn 0.8s ease-out forwards;
    }
</style>
"""

def apply_neon_style():
    display(HTML(neon_css))
    # Configuración de Seaborn para fondo oscuro
    sns.set_theme(style="darkgrid", palette="husl")
    plt.rcParams.update({
        "figure.facecolor": "#0d1117",
        "axes.facecolor": "#0d1117",
        "axes.edgecolor": "#00f3ff",
        "axes.labelcolor": "#e6edf3",
        "xtick.color": "#e6edf3",
        "ytick.color": "#e6edf3",
        "grid.color": "#21262d",
        "text.color": "#e6edf3"
    })
    print("✨ Estética Neon Dark Activada ✨")

# 2. Funciones de Limpieza Modulares
def clean_data(df_ven, df_mar, df_cli):
    # Ventas
    df_v = df_ven.copy()
    if 'precio' in df_v.columns:
        df_v.rename(columns={'precio': 'precio_unitario'}, inplace=True)
        df_v['precio_unitario'] = df_v['precio_unitario'].replace('[\$,]', '', regex=True).astype(float)
    
    df_v['fecha_venta'] = pd.to_datetime(df_v['fecha_venta'], dayfirst=True)
    df_v['venta_neta'] = df_v['precio_unitario'] * df_v['cantidad']
    df_v.dropna(subset=['venta_neta'], inplace=True)
    
    # Marketing
    df_m = df_mar.copy()
    df_m['fecha_inicio'] = pd.to_datetime(df_m['fecha_inicio'], dayfirst=True)
    df_m['fecha_fin'] = pd.to_datetime(df_m['fecha_fin'], dayfirst=True)
    
    # Corregir fechas invertidas
    mask = df_m['fecha_inicio'] > df_m['fecha_fin']
    df_m.loc[mask, ['fecha_inicio', 'fecha_fin']] = df_m.loc[mask, ['fecha_fin', 'fecha_inicio']].values
    
    return df_v, df_m, df_cli

# 3. Función de ROI Interactiva
def plot_neon_roi(roi_df):
    fig = px.bar(
        roi_df.reset_index(), 
        x='canal', 
        y='ROI',
        color='ROI',
        text_auto='.2f',
        title='🚀 Retorno de Inversión (ROI) por Canal',
        color_continuous_scale=['#ff00ff', '#00f3ff', '#39ff14'],
        template='plotly_dark'
    )
    
    fig.update_layout(
        plot_bgcolor='#0d1117',
        paper_bgcolor='#0d1117',
        font_color='#e6edf3',
        xaxis_title="Canal de Marketing",
        yaxis_title="ROI (Veces)",
        glowcolor='#00f3ff'
    )
    
    fig.show()

# 4. Branding Papiweb 3D Metal con Luz Dinámica
def show_papiweb_branding():
    branding_html = """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@900&display=swap');
        
        .papiweb-container {
            padding: 50px 0;
            text-align: center;
            background: #000;
            perspective: 1000px;
        }
        
        .papiweb-text {
            font-family: 'Orbitron', sans-serif;
            font-size: 4em;
            font-weight: 900;
            text-transform: uppercase;
            letter-spacing: 5px;
            
            /* Efecto Metalizado */
            background: linear-gradient(
                to bottom,
                #ffffff 0%,
                #e1e1e1 20%,
                #7a7a7a 50%,
                #d1d1d1 80%,
                #ffffff 100%
            );
            background-size: 200% auto;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            
            /* Efecto 3D */
            text-shadow: 
                0 1px 0 #ccc,
                0 2px 0 #c9c9c9,
                0 3px 0 #bbb,
                0 4px 0 #b9b9b9,
                0 5px 0 #aaa,
                0 6px 1px rgba(0,0,0,.1),
                0 0 5px rgba(0,0,0,.1),
                0 1px 3px rgba(0,0,0,.3),
                0 3px 5px rgba(0,0,0,.2),
                0 5px 10px rgba(0,0,0,.25),
                0 10px 10px rgba(0,0,0,.2),
                0 20px 20px rgba(0,0,0,.15);
            
            display: inline-block;
            transform: rotateX(20deg);
            animation: metalShine 3s linear infinite, floatText 4s ease-in-out infinite;
        }
        
        .papiweb-sub {
            color: #00f3ff;
            font-family: 'Courier New', monospace;
            font-size: 1.2em;
            letter-spacing: 10px;
            text-shadow: 0 0 10px #00f3ff;
            margin-top: -10px;
            animation: pulseNeon 2s infinite alternate;
        }

        /* Animación de la luz dinámica sobre el metal */
        @keyframes metalShine {
            to {
                background-position: 200% center;
            }
        }
        
        /* Animación de flotación 3D */
        @keyframes floatText {
            0%, 100% { transform: rotateX(20deg) translateY(0); }
            50% { transform: rotateX(25deg) translateY(-15px); }
        }
        
        @keyframes pulseNeon {
            from { opacity: 0.5; text-shadow: 0 0 5px #00f3ff; }
            to { opacity: 1; text-shadow: 0 0 20px #00f3ff; }
        }
    </style>
    
    <div class="papiweb-container">
        <div class="papiweb-text">PAPIWEB</div><br>
        <div class="papiweb-sub">Desarrollos Informáticos</div>
    </div>
    """
    display(HTML(branding_html))
