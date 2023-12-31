#  Đồ Án Kết Thúc Học Phần NTO30102 Chuyên đề công nghệ mới !

***

## Mục Lục

1. [Tổng quan](#1-tổng-quan)
   - [Giới Thiệu](#giới-thiệu)
   - [Mục Đích](#mục-đích)

2. [Thông tin thành viên](#2-thông-tin-thành-viên)

3. [Demo](#3-demo)
   - [Hình ảnh](#hình-ảnh)
   - [Kết nối](#kết-nối)
   - [Giao Diện](#giao-diện)
   - [Video](#video)

4. [Deploy source code](#4-deploy-source-code)
   - [Giao diện](#1-giao-diện)
   - [Luồng dữ liệu](#2-luồng-dữ-liệu)
   - [Orther](#3-orther)
   - [Environment](#4-environment)

***

## 1 Tổng quan 

### Giới Thiệu

> Dự án này đặt ra một cơ sở thông qua việc ứng dụng công nghệ Blockchain. Mục tiêu chính của Nhóm là tạo ra một hệ thống giúp truy xuất nguồn gốc của lâm sản, đặc biệt là đối với lĩnh vực gỗ. Việc này không chỉ giúp xác định nguồn gốc một cách chính xác mà còn đảm bảo tính minh bạch và quyền sở hữu của chuỗi cung ứng.

> Trong một thế giới nơi mà vấn đề về bảo vệ môi trường và quản lý nguồn lâm sản đang trở thành ngày càng quan trọng, dự án của nhóm không chỉ là một nỗ lực trong việc ứng dụng công nghệ mới mẻ mà còn là sự đóng góp xã hội. Nhóm hy vọng rằng việc xây dựng một hệ thống như vậy sẽ không chỉ giúp doanh nghiệp và người tiêu dùng trong việc theo dõi nguồn gốc của sản phẩm mà còn góp phần vào việc bảo vệ môi trường và phát triển cộng đồng.
***
### Mục đích 
- 1 Truy xuất thông tin lâm sản
- 2 Lưu trữ và quản lý thông tin
- 3 Áp dụng công nghệ Blokcchain, bảo mật và minh bạch





## 2 Thông tin thành viên
- [ Nguyễn Thái Dương ](https://github.com/ddryuu)
   > **ID:** Mã ID 2051220053
   > **Role:** Member - 20CT2
- [ Nguyễn Hoàng Linh ](https://github.com/hoanglinh-wieee)
   > **ID:** Mã ID 2051220165
   > **Role:** Leader - 20CT2
- [ Phan Thị Việt Nga ](https://github.com/ptvnga)
   > **ID:** Mã ID 2051220091
   > **Role:** Member - 20CT2



***

## 3 Demo 
### Hình ảnh 

<p align="center">
  <img src="https://github.com/ddryuu/Trace-the-origin-of-forest-product/assets/118073917/218fdc0e-718e-4f4e-b55a-2e4e932f224a" alt="Trang chủ" width="700">
</p>
<p align="center">Trang chủ</p>

### Kết nối
<p align="center">
  <img width="700" height="350" src="https://github.com/ddryuu/Trace-the-origin-of-forest-product/assets/118073917/934fb03b-917a-45d9-a6c5-80efc4ad954e" alt="Mô tả ảnh">
</p>

<p align="center">kết nối</p>

### Giao Diện
<p align="center">
  <img width="700" height="320" src="https://github.com/ddryuu/Trace-the-origin-of-forest-product/assets/118073917/0e39ce5f-e198-40d6-a312-7e23447b783c" alt="Mô tả ảnh">
</p>

<p align="center">giao diện</p>

### Video

<p align="center">
  <a href="https://www.youtube.com/watch?v=rflvMoBPebQ&t=1s">
    <img src="https://wallpapers.com/images/hd/aerial-view-pine-trees-4k-forest-7sfd6znw2ry6hnlt.jpg" width="700" alt="Demo video">
  </a>
</p>






***

## 4 Deploy source code
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
- [Đưa dữ liệu thông truy xuất](https://github.com/ddryuu/Trace-the-origin-of-forest-product/blob/main/app/template/ttraceability.html)
```
 {% for item in info %}

        <tr>
            <td>
                {{ item.product.name }}
            </td>
            <td>
                {{ item.actor.name }}
            </td>
        
        </tr>
    {% endfor %}
```
### 3 Orther
- [backup source code](https://github.com/ddryuu/Trace-the-origin-of-forest-product/tree/main/extra/weblamsan)
### 4 Environment
- [Framework](https://www.djangoproject.com/)
- [Blockchain](https://www.blockchain.com/)
- [Metamask](https://metamask.io/)
- [Tutorial](https://www.djangoproject.com/start/)
- [Python](https://www.python.org/)
***
### Thanks!!
