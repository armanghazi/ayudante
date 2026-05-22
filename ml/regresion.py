import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from visualizaciones.regresiones import par_real_predicho, par_real_predicho_res


def evaluar_modelo(modelo, X_test, y_test, magnitud=""):
    """
    Evalúa automáticamente cualquier modelo de regresión.
    Genera métricas, gráficos y devuelve un diccionario con resultados.
    """

    # 1) Predicciones
    y_pred = modelo.predict(X_test)

    # 2) Métricas
    mae = mean_absolute_error(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    r2 = r2_score(y_test, y_pred)

    # 3) Gráficos
    par_real_predicho(y_test, y_pred, magnitud)
    resumen_residuos = par_real_predicho_res(y_test, y_pred, magnitud)

    # 4) Resumen
    resultados = {
        "MAE": mae,
        "RMSE": rmse,
        "R2": r2,
        "mean_residual": resumen_residuos["mean_residual"],
        "std_residual": resumen_residuos["std_residual"],
        "mae_residual": resumen_residuos["mae"],
        "rmse_residual": resumen_residuos["rmse"]
    }

    print("\n📊 RESULTADOS DEL MODELO")
    print("-------------------------")
    print(f"MAE:  {mae:.4f}")
    print(f"RMSE: {rmse:.4f}")
    print(f"R2:   {r2:.4f}")
    print("-------------------------")
    print("Diagnóstico de residuos:")
    print(f"Media residuos: {resultados['mean_residual']:.4f}")
    print(f"STD residuos:   {resultados['std_residual']:.4f}")

    return resultados
