
EFS 마운트 헬퍼 설치
```
sudo dnf install -y amazon-efs-utils
```

마운트 포인트 생성
```
sudo mkdir /<file path>

sudo mount -t efs <file-system-id>:/ /<file-path>
```
