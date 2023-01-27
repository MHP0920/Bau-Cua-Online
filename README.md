# Bầu Cua Online Game - Chuyển đổi số trò chơi dân gian 🐧
## Mở đầu
Hôm nay đã là mùng 6, đầu mùng 7 Tết rồi, là ngày may mắn để mọi người khai xuân, khai sách, và cả khai code nữa :)

Nên mình quyết định dành ra từ mùng 1 đến giờ chỉ để design và viết code trò chơi Bầu Cua Online này, mong các bạn sẽ ủng hộ để tụi mình tiếp tục ra thêm nhiều sản phẩm nữa :)
## Hành trình
Mình bắt đầu lên ý tưởng từ mùng 1 sau khi lướt qua tận 2 bài viết về bầu cua nhưng đa phần chỉ là chơi đơn và ở trên website, nên mình quyết định vào design app trước và vẻ lộ trình sau khi đã có bản thiết kế. Ban đầu mình chỉ nghĩ là làm cho vui với lại chỉ chạy localhost thôi nên không tính đến chuyện code server có thể chạy nhiều người, nhưng mà đam mê của mình từ nhỏ là game online multiplayer nên thôi vậy 🤡

Mùng 2, 3 thì mình đi ăn chơi với nhận lì xì nên không để ý tới project lắm, sướng trước khổ sau không sao cả 🐧

Nhưng mà về đêm thì mình vẫn ngồi nghĩ cách làm, tại thực sự thì đây là lần đầu mình làm game online nhiều người chơi, thêm việc lâu ngày không code app khiến mình lú cái đầu thiệt luôn 😔

Mùng 4, 5, lúc này mình mới thực sự chú tâm để hoàn thiện project, nhưng mà có hơi "lười" nên hôm nay mình mới đăng bài trễ như vậy, tại chạy deadline từ 4h sáng mùng 6 đến 12h đêm luôn mà 💀

Lên ý tưởng không quá khó, mình lên tìm hiểu cách làm game online ở những channel như freeCodeCamp, Techwithtim, và vì họ đã có source mẫu nên việc code của mình dễ hơn khá nhiều (Mình thường đọc cách vận hành của code thay vì ngồi xem tutorial)

Vậy là code đã xong hết, mình phải ngồi lại debug tận 2 tiếng mới chắc chắn, nhưng còn 1 vấn đề... Máy chủ để chạy game online. Mình biết hiện nay có rất nhiều nơi cho thuê dịch vụ host máy chủ miễn phí hoặc giá rẻ, nhưng host game lại là một câu chuyện khác, đặc biệt là game online. Vì đặc tính cần kết nối thời gian thực của nó nên nhiều loại host giá rẻ hoặc miễn phí không thể đáp ứng được, kể cả dịch vụ mình đang dùng nên mình và bạn [Notch Apple](https://www.facebook.com/notchapple1703) đã ngồi vọc vạch đủ thứ để tìm ra cách host rẻ nhất có thể (Vì là Open-source Project) nên mình đâu kiếm tiền được :<
## Cách chơi
Mình có viết hướng dẫn ngay trong trò chơi, các bạn có thể vào trang chủ của app rồi nhấn vào nút "Đọc hướng dẫn" nha.
## Cách tải về
**Nếu như bạn có git, dùng lệnh:**
> git clone https://github.com/MHP0920/Bau-Cua-Online.git

> cd Bau-Cua-Online

Vì đã có host public nên bạn chỉ việc chạy trong thư mục client, mà nhớ chỉnh sửa lại username trong tệp customize.json nhé.
> cd client

> python main.py

Với những bạn không có git có thể tải code và giải nén ra nhé, rồi dùng lệnh `cd` như trên là được.

**Với những bạn có máy chủ của riêng mình:**
Lệnh tương tự, nhưng bạn gọi thêm 1 cmd và `cd` vào thư mục `server`
> cd server

> python main.py

Sau đó bạn config file customize.json ở client phần host và port về máy chủ của bạn là được.
## Credit
**Coding and Designing, Debugging and Final Releasing**

[Trần Minh Hiếu](https://facebook.com/py.hacker.hieu)

**Hosting, Server Managing and Supporting**

[Notch Apple](https://www.facebook.com/notchapple1703)

Made by MHP Team with 💖
