
EFS 마운트 헬퍼 설치
```
sudo dnf install -y amazon-efs-utils
```

마운트 포인트 생성
```
sudo mkdir /mnt/efs #EFS 마운트할 디렉토리 생성

sudo mount -t efs <file-system-id>:/ /mnt/efs #EFS 파일 시스템을 해당 디렉토리에 연결
```
