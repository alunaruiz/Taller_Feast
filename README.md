# Taller_Feast
Taller sobre Feast, orientado a la gestión y servicio de características para enriquecer tus datos y proporcionar características en tiempo real a tus modelos.

#Qué es Feast?

Feast es una plataforma para administrar y servir características (features) en aplicaciones de aprendizaje automático. Aunque ya tengas un modelo en experimentación con MLflow y almacenado en MinIO, Feast puede ser útil para enriquecer tus datos de entrada con características adicionales antes de pasarlos al modelo.

Aquí hay algunas formas en las que Feast puede complementar tu flujo de trabajo con MLflow y MinIO:

1. Gestión de características: Feast proporciona una forma conveniente de definir, almacenar y gestionar características de manera centralizada. Puedes definir y registrar tus características en Feast, lo que facilita su reutilización en diferentes modelos y experimentos. Esto ayuda a mantener un catálogo centralizado de características y asegura la coherencia en su uso.

2. Preprocesamiento de características: Feast puede ayudarte a realizar el preprocesamiento de características antes de alimentarlas a tu modelo. Puedes aplicar transformaciones y agregaciones a las características, como normalización, codificación one-hot, discretización, entre otras. Esto te permite realizar el procesamiento necesario de las características antes de entrenar o inferir con tu modelo.

3. Servicio de características en tiempo real: Feast puede servir características en tiempo real para su uso en aplicaciones y servicios en producción. Puedes configurar un servicio de características con Feast para que esté disponible para tu modelo en producción y otros sistemas en tiempo real. Esto permite que tus modelos accedan a características actualizadas y enriquecidas en tiempo real durante la inferencia.

4. Integración con MLflow: Feast se puede integrar con MLflow para proporcionar una solución completa para el desarrollo, seguimiento y despliegue de modelos de aprendizaje automático. Puedes utilizar Feast para obtener características enriquecidas durante el entrenamiento y la inferencia de tus modelos de MLflow. Además, Feast proporciona integraciones con otras herramientas populares de la comunidad de aprendizaje automático, como TensorFlow, PyTorch y Scikit-learn.

5. En resumen, mientras que MLflow y MinIO se centran en el seguimiento y almacenamiento de modelos, Feast se enfoca en la gestión y servicio de características para enriquecer tus datos y proporcionar características en tiempo real a tus modelos. Si deseas mejorar tus modelos con características adicionales y mantener un catálogo centralizado de características, Feast puede ser una herramienta valiosa en tu flujo de trabajo de aprendizaje automático.
