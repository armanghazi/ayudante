from .correlacion import heatmap_corr
from .regresiones import par_real_predicho, par_real_predicho_res

__all__ = ["heatmap_corr", "par_real_predicho", "par_real_predicho_res"]

from .eda import reporte_eda, resumen_general, estadisticos
__all__.extend(["reporte_eda", "resumen_general", "estadisticos"])

