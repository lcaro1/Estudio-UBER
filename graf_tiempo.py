import os
import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
from matplotlib.ticker import MultipleLocator
import datetime as dt

sns.set(rc={"axes.facecolor":"#FFFFFF", "axes.edgecolor": "#000000", "axes.grid":True, "axes.grid.which":"major", "axes.grid.axis": "x",
                "grid.color": "#b9b7bd", "grid.alpha": 1, "grid.linestyle": "-", "grid.linewidth": 0.5, "axes.xmargin": 0.0, "axes.ymargin": 0.0,
                "text.color": ".15", "xtick.color": ".15",  "xtick.direction": "out", "xtick.top": False, "xtick.bottom": True, "ytick.color": ".15",
                "ytick.direction": "out", "ytick.left": True, "ytick.right": False, "axes.spines.top": False, "axes.spines.bottom": True,
                "axes.spines.left": True, "axes.spines.right": False, "xtick.major.width": 0.8, "xtick.major.pad": 1, "ytick.major.width": 0.8,
                "ytick.major.pad": 0, "xtick.minor.visible": True,  "xtick.minor.size": 3, "xtick.minor.width": 1, "xtick.minor.pad": 1, 
                "ytick.minor.visible": True, "ytick.minor.size": 3,"ytick.minor.width": 1, "ytick.minor.pad": 1, "date.autoformatter.day": "%d-%b"})


def graf_tiempo (df_uber):
    fig, ax = plt.subplots(figsize=(16,8))
            
    plt.suptitle("Tiempos de viaje promedio por día", fontsize = 25, fontweight = "bold", ha= "center", va = "top")
    plt.title("Primer trimestre Año 2020", fontsize = 14, fontweight = "normal", loc = "center", y = 1, pad = 20)# loc='left', loc='right' verticalalignment ('top', 'bottom', 'center', 'baseline')
    plt.xlabel (" ", fontsize = 0, labelpad = 0)
    plt.ylabel ("Tiempo (en minutos)", fontsize = 20, labelpad = 10)


    sns.lineplot(data=df_uber, x=df_uber.date, y=df_uber.mean_travel_time, estimator="mean", ci=None,
                        lw=3, marker = "o", color = 'purple', legend=False) # palette= ["#eeede7"]

    plt.axhline(y=np.mean(df_uber.mean_travel_time), color="red", linestyle="--", lw =2.5)


        # Set Interval eje x e Y
    plt.xticks(np.arange(dt.date(2019,12,30),dt.date(2020,3,31),7), fontsize=18, rotation = 30)
    plt.yticks(np.arange(0, 25, 5), fontsize=18)
    ax.axes.xaxis.set_minor_locator(MultipleLocator(1))

            # anotaciones puntos criticos

    ax.annotate("Año\nNuevo", xy=(dt.date(2020,1,1), 12.655), xycoords = "data",
                    xytext=(50, 20), textcoords = "offset points", fontsize = 12, ha = "center", va = "top",
                    arrowprops=dict(arrowstyle = "->", color = "black", shrinkA = 1, shrinkB = 2, 
                                    connectionstyle = "arc3,rad=0.3")) #, shrink=0.05,
        
    # ax.annotate("Inicio de mes\nFebrero", xy = (dt.date(2020,2,1), 12.249), xycoords = "data",
    #             xytext=(60, 30), textcoords = "offset points", fontsize = 12, ha = "center", va = "top",
    #             arrowprops=dict(arrowstyle = "->", color = "black", shrinkA = 1, shrinkB = 2, 
    #                             connectionstyle = "arc3,rad=0.3")) #  , shrink=0.05

    # ax.annotate("Fin\nVaciones", xy = (dt.date(2020,2,29), 12.471), xycoords = "data",
    #             xytext=(40, 80), textcoords = "offset points", fontsize = 12, ha = "center", va = "top",
    #             arrowprops=dict(arrowstyle = "->", color = "black", shrinkA = 1, shrinkB = 2, 
    #                             connectionstyle = "arc3,rad=0.3")) #  , shrink=0.05

    ax.annotate("Suspensión de\nclases", xy = (dt.date(2020,3,16), 11.89), xycoords = "data",
                    xytext=(60, 40), textcoords = "offset points", fontsize = 12, ha = "center", va = "top",
                    arrowprops=dict(arrowstyle = "->", color = "black", shrinkA = 1, shrinkB = 2, 
                                    connectionstyle = "arc3,rad=0.3")) #  , shrink=0.05

    ax.annotate("Inicio\nCuarentena", xy = (dt.date(2020,3,26), 10.50), xycoords = "data",
                    xytext=(1, 50.0), textcoords = "offset points", fontsize = 12, ha = "center", va = "top",
                    arrowprops=dict(arrowstyle = "->", color = "black", shrinkA = 1, shrinkB = 2, 
                                    connectionstyle = "arc3,rad=-0.3")) #  , shrink=0.05

        # Set legend
    plt.legend(title = "Registros de viajes", loc='best', handlelength = 2, handleheight= 0.3, ncol= 1, facecolor= 'inherit', 
                    fontsize='large' , edgecolor = 'black', shadow=False, labels =["Viajes", "Media"]) #, bbox_to_anchor=(0.55, -0.1)
        

    plt.show()
    # plt.savefig("Graficos/Figure_3.png", dpi=800)


def graf_tiempo_rango (df_uber):
    fig, ax = plt.subplots(figsize=(16,8))
            
    plt.suptitle("Tiempos de viaje promedio por día según rango horario", fontsize = 25, fontweight = "bold", ha= "center", va = "top")
    plt.title("Primer trimestre Año 2020", fontsize = 14, fontweight = "normal", loc = "center", y = 1, pad = 15)# loc='left', loc='right' verticalalignment ('top', 'bottom', 'center', 'baseline')
    plt.xlabel (" ", fontsize = 0, labelpad = 0)
    plt.ylabel ("Tiempo (en minutos)", fontsize = 20, labelpad = 10)

        #     # set Grafico

    sns.lineplot(data=df_uber, x=df_uber.date, y=df_uber.mean_travel_time, hue = "cat_time_range", estimator="mean", ci=None,
                        lw=1.5, marker = "o", palette= ['green', 'purple', 'blue', 'orange', 'red'], legend=False)

    plt.axhline(y=np.mean(df_uber.mean_travel_time), color="black", linestyle="--", lw =2.5)


            # # Set Interval eje x e y

    plt.xticks(np.arange(dt.date(2019,12,30),dt.date(2020,3,31),7), fontsize=18, rotation = 30)
    plt.yticks(np.arange(0, 25, 5), fontsize=18)
    ax.axes.xaxis.set_minor_locator(MultipleLocator(1))

            # anotaciones puntos criticos
    ax.annotate("Año\nNuevo", xy=(dt.date(2020,1,1), 16.315), xycoords = "data",
                    xytext=(50, 10), textcoords = "offset points", fontsize = 12, ha = "center", va = "top",
                    arrowprops=dict(arrowstyle = "->", color = "black", shrinkA = 1, shrinkB = 2, 
                                    connectionstyle = "arc3,rad=0.3")) #, shrink=0.05,

    # ax.annotate("Inicio de mes\nFebrero", xy = (dt.date(2020,2,1), 13.646), xycoords = "data",
    #             xytext=(60, 30), textcoords = "offset points", fontsize = 12, ha = "center", va = "top",
    #             arrowprops=dict(arrowstyle = "->", color = "black", shrinkA = 1, shrinkB = 2, 
    #                             connectionstyle = "arc3,rad=0.3")) #  , shrink=0.05

    # ax.annotate("Fin\nVaciones", xy = (dt.date(2020,2,29), 13.452), xycoords = "data",
    #             xytext=(30, 80), textcoords = "offset points", fontsize = 12, ha = "center", va = "top",
    #             arrowprops=dict(arrowstyle = "->", color = "black", shrinkA = 1, shrinkB = 2, 
    #                             connectionstyle = "arc3,rad=0.3")) #  , shrink=0.05

    ax.annotate("Suspensión de\nclases", xy = (dt.date(2020,3,16), 13.444), xycoords = "data",
                    xytext=(60, 40), textcoords = "offset points", fontsize = 12, ha = "center", va = "top",
                    arrowprops=dict(arrowstyle = "->", color = "black", shrinkA = 1, shrinkB = 2, 
                                    connectionstyle = "arc3,rad=0.3")) #  , shrink=0.05
            
    ax.annotate("Inicio\nCuarentena", xy = (dt.date(2020,3,26), 11.962), xycoords = "data",
                    xytext=(1, 50.0), textcoords = "offset points", fontsize = 12, ha = "center", va = "top",
                    arrowprops=dict(arrowstyle = "->", color = "black", shrinkA = 1, shrinkB = 2, 
                                    connectionstyle = "arc3,rad=-0.3")) #  , shrink=0.05

            # Set legend

    plt.legend(title = "Rango horario", loc=3, handlelength = 2, handleheight= 0.3, ncol= 6, facecolor= 'inherit', 
                    fontsize='large' , edgecolor = 'black', shadow=False, markerscale=1, markerfirst=True,
                    labels =["0-7", "7-10", "10-16", "16-19", "19-0", "Media"]) #, bbox_to_anchor=(1.0, 1.0)

    plt.show()
    # plt.savefig("Graficos/Figure_4.png", dpi=800)


def main ():

    os.chdir("C:/Users/BabyPink/Documents/Estudio_UBER/")
    df = pd.read_csv("dataframes/preparados/df_uber.csv", sep=",", parse_dates= ["date"], 
                     dtype={"sourceid": np.int16, "dstid":np.int16, "day_name":np.int8 , "cat_time_range":np.int8, 
                            "mean_travel_time":np.float32, "standard_deviation_travel_time": np.float32, "dist_kms":np.float32, 
                            "vel_kms_hr": np.float32, "cancelado":np.int8, "resultado":np.int8})
    
    # pd.set_option('display.max_columns', 13)
    # pd.set_option('display.float_format', lambda x: '%.5f' % x)

    graf_tiempo(df)
    graf_tiempo_rango(df)
    print("listo!!")
    
    
if __name__ == "__main__":
    main()
