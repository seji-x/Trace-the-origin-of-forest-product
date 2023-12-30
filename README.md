#  Đồ Án Kết Thúc Học Phần NTO30102 Chuyên đề công nghệ mới !

***


## 1 Giới Thiệu



> Dự án này đặt ra một cơ sở thông qua việc ứng dụng công nghệ Blockchain. Mục tiêu chính của Nhóm là tạo ra một hệ thống giúp truy xuất nguồn gốc của lâm sản, đặc biệt là đối với lĩnh vực gỗ. Việc này không chỉ giúp xác định nguồn gốc một cách chính xác mà còn đảm bảo tính minh bạch và quyền sở hữu của chuỗi cung ứng.

> Trong một thế giới nơi mà vấn đề về bảo vệ môi trường và quản lý nguồn lâm sản đang trở thành ngày càng quan trọng, dự án của nhóm không chỉ là một nỗ lực trong việc ứng dụng công nghệ mới mẻ mà còn là sự đóng góp xã hội. Nhóm hy vọng rằng việc xây dựng một hệ thống như vậy sẽ không chỉ giúp doanh nghiệp và người tiêu dùng trong việc theo dõi nguồn gốc của sản phẩm mà còn góp phần vào việc bảo vệ môi trường và phát triển cộng đồng.



---



## 2 Thông tin thành viên
- Nguyễn Thái Dương 
   >- **ID:** Mã ID 2051220053
   >- **:** Member - 20CT2
- Nguyễn Hoàng Linh 
   >- **ID:** Mã ID 2051220165
   >- **:** Leader - 20CT2
- Tên Thành Viên 
   >- **ID:** Mã ID 2051220094
   >- **:** Member - 20CT2



***

## 3 Demo 
### Hình ảnh 

<p align="center">
  <img src="https://github.com/ddryuu/Trace-the-origin-of-forest-product/assets/118073917/218fdc0e-718e-4f4e-b55a-2e4e932f224a" alt="Trang chủ" width="900">
</p>
<p align="center">Trang chủ</p>

<p align="center">
  <img src="https://github.com/ddryuu/Trace-the-origin-of-forest-product/assets/118073917/b6e969cc-9080-49c2-9ee1-b66bf04264f2[vvvvvv](https://github.com/ddryuu/Trace-the-origin-of-forest-product/assets/118073917/70fb844d-c0a4-4895-9b75-17df096a77a4)
" alt="Trang chủ" width="900">
</p>
<p align="center">Đăng nhập</p>

[Click here to watch the topic via video](https://www.youtube.com/watch?v=rflvMoBPebQ)

***

## Deploy source code
### 1 Giao diện 
- [Static/App](https://github.com/ddryuu/Trace-the-origin-of-forest-product/tree/main/app/static/app)
- [templates](https://github.com/ddryuu/Trace-the-origin-of-forest-product/tree/main/app/template)
  
### 2 Luồng dữ liệu
- [Blockchain_web3](https://github.com/ddryuu/Trace-the-origin-of-forest-product/tree/main/app/blockchain_web3)
- [Setup Data](https://github.com/ddryuu/Trace-the-origin-of-forest-product/blob/main/app/blockchain_web3/fakedata.py)
```
if __name__ == "__main__":
    account = Account.create()
    address = account.key.hex()
    usr = [create_user(0, "cty a", "aaa"), create_user(1, "cty b", "bbb"), create_user(2, "cty c", "ccc")]
    deposited_actor(usr[1])
    deposited_actor(usr[2])
    p1 = create_product(1, "", usr[0], "cay go c", "")
    t1 = buy_product(p1, 100, usr[1])
    p2 = create_product(2, t1, usr[1], "tu bep", "")
    t2 = buy_product(p2, 100, usr[2])
    p3 = create_product(3, t2, usr[2], "tu bep", "")
    print(p3)

    data = traceability.get_info_product(p3)
    for item in data:
        print(item)
        print(ProductProvider.convert_data(item[0]), ActorProvider.convert_data_user(item[1]))
```
- [Đưa dữ liệu ra Gui](https://github.com/ddryuu/Trace-the-origin-of-forest-product/blob/main/app/template/home.html)
```
<div class="container">
        <div class="row">
            <!-- Cột lớn 3 chứa ảnh thứ nhất -->
            {% for product in products %}
                
                <div class="col-lg-3">
                    <div class="thumbnail-container">
                        <img class="thumbnail" src="{% static 'app/images/gomun.png' %}">
                        <div class="box-element product">
                            <h6><strong> {{ product.name }} </strong></h6>
                            <hr>
                            {% if product.product_type > 1 %}
                            <p> gỗ đã qua gia công </p>
                            {% else %}
                            <p> gỗ thô</p>
                            {% endif %}
                            <a class="btn btn-outline-secondary add-btn " href="traceability/{{ product.id }}">  Tra Cứu</a>
                            <a class="btn btn-outline-success" href="wood/read/{{ product.id }}">Xem Thông Tin Gỗ</a>
                            <h2 style="display: inline-block; float: right"><strong> </strong></h2>
                        </div>
                        
                    </div>
                </div>
```
- [Đưa dữ liệu thông tin](https://github.com/ddryuu/Trace-the-origin-of-forest-product/blob/main/app/template/about.html)
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <table>
        <tr>
            <th>key</th>
            <th>infomation</th>
        </tr>
        <tr>
            <td>id</td>
            <td>{{ product.id }}</td>
        </tr>
        <tr>
            <td>type</td>
            <td>{{ product.product_type }}</td>
        </tr>
        <tr>
            <td>price</td>
            <td>{{ product.price }}</td>
        </tr>
        <tr>
            <td>owner id</td>
            <td>{{ product.owner }}</td>
        </tr>
        <tr>
            <td>name</td>
            <td>{{ product.name }}</td>
        </tr>
    </table>
</body>
</html>
```

## Bản Quyền và Giấy Phép

Thông tin về bản quyền và giấy phép sử dụng của dự án.


***

## Mục Lục

1. [Giới Thiệu](#giới-thiệu)
2. [Thông tin thành viên](#Thông-tin-thành-viên)
3. [Cách Sử Dụng](#cách-sử-dụng)
4. [Cài Đặt Môi Trường](#cài-đặt-môi-trường)
5. [Demo](#Demo-Giao-Diện)
6. [Bản Quyền và Giấy Phép](#bản-quyền-và-giấy-phép)
