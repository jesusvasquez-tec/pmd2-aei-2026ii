import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(page_title="AndeHogar Analytics", page_icon="🏠", layout="wide")

st.title("🏠 AndeHogar · Dashboard de Decisión Gerencial")
st.markdown("Panel de control para la campaña de retención y reposición de **noviembre 2026**.")
st.caption("Fecha de actualización: 2026-11-04 | Importes en soles (S/)")

st.divider()

# Sidebar para navegación
menu = st.sidebar.selectbox(
    "Menú de Navegación", 
    ["Resumen Ejecutivo", "Pronóstico de Demanda", "Optimización PuLP", "Gobierno y Procesos", "Asistente Analítico"]
)

if menu == "Resumen Ejecutivo":
    st.header("📊 KPIs de la Decisión Óptima")
    col1, col2, col3 = st.columns(3)
    col1.metric("Mejora de Margen", "+22.0%", "S/ 6,515.53 adicionales")
    col2.metric("Contactos WhatsApp", "451", "vs 600 de la política actual")
    col3.metric("Clientes sin Consentimiento", "0", "Cumplimiento Ley 29733")

    st.info("💡 **Hallazgo Clave:** La política actual es infactible (excede almacén y presupuesto). El modelo PuLP optimiza el contacto priorizando CLV sobre recencia, logrando mayor margen con menos contactos.")

elif menu == "Pronóstico de Demanda":
    st.header("📈 Pronóstico Holt-Winters (Próximas 4 Semanas)")
    st.write("Total pronosticado: **1,209 unidades**")
    
    datos_pronostico = {
        "Línea": ["Cocina menor", "Electrodomésticos", "Organización", "Textiles", "Iluminación", "Limpieza"],
        "Total 4 Semanas": [291, 111, 224, 230, 181, 173]
    }
    df = pd.DataFrame(datos_pronostico).set_index("Línea")
    st.bar_chart(df, use_container_width=True)

elif menu == "Optimización PuLP":
    st.header("⚖️ Política Actual vs. Solución Óptima")
    df_comp = pd.DataFrame({
        "Métrica": ["Margen Total (S/)", "Contactos WA", "Uso Almacén (unidades)"],
        "Política Actual (Ajustada)": [29609.98, 600, 799.4],
        "Solución Óptima PuLP": [36125.51, 451, 787.4]
    })
    st.dataframe(df_comp, use_container_width=True)
    st.warning("⚠️ **Nota:** La política original viola las restricciones de almacén (883 > 800) y presupuesto. Se aplicó un factor de ajuste de 0.9055 para la comparación justa.")

elif menu == "Gobierno y Procesos":
    st.header("🛡️ Control y Cumplimiento")
    st.markdown("- **Carta de Control:** 0 alertas en 1,341 días de monitoreo. Proceso estable.")
    st.markdown("- **Auditoría de Consentimiento:** 50 clientes de la política original fueron descartados por no tener consentimiento (*Privacy by Design*).")
    st.markdown("- **Explicabilidad (SHAP):** El CLV a 6 meses es 5 veces más predictivo que la recencia para anticipar el churn.")

elif menu == "Asistente Analítico":
    st.header("🤖 Evaluación del Asistente Text-to-SQL")
    st.markdown("El asistente opera en modo **solo lectura** con validación de seguridad (bloqueo de DROP/DELETE).")
    col1, col2 = st.columns(2)
    col1.metric("Tasa de Acierto", "95.0%", "Incluye abstenciones correctas")
    col2.metric("Tasa de Alucinación", "5.0%", "Detectada en preguntas ambiguas")
    
    st.subheader("Ejemplo de Línea Base Determinista")
    st.code("SELECT COUNT(id_cliente) FROM clientes WHERE consentimiento_contacto = 1;", language="sql")
    st.caption("Consulta segura y verificable para preguntas legítimas.")

st.divider()
st.markdown("Desarrollado por el Equipo de Analítica Empresarial | PMD2 2026-II")
