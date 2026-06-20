# Web örnek kullanım

Kendi notum gibi yazdım, amaç sadece akışı göstermek.

## Challenge

Login paneli var. Cookie içinde base64 gibi duran bir değer var.

## Sorulacak örnek

```txt
@ctf login sayfasında cookie var, role=user gibi duruyor. Nereden başlayayım?
```

## Beklenen akış

1. Cookie decode edilir.
2. Role, user id, imza veya JWT mi diye bakılır.
3. Değer değiştirince hata/başarı farkı kontrol edilir.
4. Eğer JWT ise header/payload/alg kontrol edilir.
5. Endpoint tarafında IDOR veya auth bypass denenir.

## Kendi kontrol listem

```bash
curl -i http://target/
echo 'cookie_degeri' | base64 -d
python3 templates/web_jwt_crack.py '<token>' rockyou.txt
```

Not: Gerçek sistemde değil, sadece challenge/lab ortamında.
