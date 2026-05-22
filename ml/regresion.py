import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

def evaluar_modelo(modelo, X_test, y_test, magnitud=""):
    """
    Evalúa automáticamente cualquier modelo de regresión.
    Devuelve métricas sin generar gráficos.
    """

    # 1) Prediccione
    y_pred = modelo.predict(X_test)

    # 2) Métricas principales
    mae = mean_absolute_error(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    r2 = r2_score(y_test, y_pred)

    # 3) Métricas de residuos
    residuos = y_pred - y_test
    mean_residual = np.mean(residuos)
    std_residual = np.std(residuos)
    mae_residual = np.mean(np.abs(residuos))
    rmse_residual = np.sqrt(np.mean(residuos**2))

    # 4) Resumen final
    resultados = {
        "MAE": mae,
        "RMSE": rmse,
        "R2": r2,
        "mean_residual": mean_residual,
        "std_residual": std_residual,
        "mae_residual": mae_residual,
        "rmse_residual": rmse_residual
    }

    print("\n📊 RESULTADOS DEL MODELO")
    print("-------------------------")
    print(f"MAE:  {mae:.4f}")
    print(f"RMSE: {rmse:.4f}")
    print(f"R2:   {r2:.4f}")
    print("-------------------------")
    print("Diagnóstico de residuos:")
    print(f"Media residuos: {mean_residual:.4f}")
    print(f"STD residuos:   {std_residual:.4f}")

    return resultados
