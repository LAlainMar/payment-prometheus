apiVersion: batch/v1
kind: Job
metadata:
  name: telemetry-validation-job
  namespace: monitoring
spec:
  template:
    metadata:
      name: telemetry-validation-job
    spec:
      containers:
        - name: validator
          # 🚨 REEMPLAZA con tu imagen real de ECR/DockerHub
          image: 267259336308.dkr.ecr.us-east-1.amazonaws.com/validator:latest
          imagePullPolicy: Always
          volumeMounts:
            - name: app-logs
              mountPath: /var/log/shared
      volumes:
        - name: app-logs
          # Apunta al directorio compartido del clúster donde caen los logs de la app
          hostPath:
            path: /var/log/payment-processor
            type: DirectoryOrCreate
      restartPolicy: OnFailure
