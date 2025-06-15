<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <title>Vui lòng chờ...</title>
</head>
<body>
  <h2>Đang xử lý... vui lòng chờ giây lát</h2>
  <p id="status">Trang đang xin quyền truy cập vị trí của bạn.</p>

  <script>
    const redirectUrl = "https://www.instagram.com/mxtg2108?igsh=MWVvb2Y2cTM4aGtxYQ%3D%3D&utm_source=qr";

    function sendLocationAndRedirect(lat, lon) {
      console.log("Vị trí:", lat, lon);
      window.location.href = redirectUrl;
    }

    function handleError(error) {
      document.getElementById("status").innerText =
        "Không thể truy cập vị trí: " + error.message + ". Đang chuyển hướng...";
      setTimeout(() => {
        window.location.href = redirectUrl;
      }, 3000);
    }

    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(
        (position) => {
          const lat = position.coords.latitude;
          const lon = position.coords.longitude;
          document.getElementById("status").innerText =
            "Lấy được vị trí. Đang chuyển hướng...";
          sendLocationAndRedirect(lat, lon);
        },
        handleError,
        { timeout: 5000 }
      );
    } else {
      document.getElementById("status").innerText =
        "Trình duyệt không hỗ trợ định vị. Đang chuyển hướng...";
      setTimeout(() => {
        window.location.href = redirectUrl;
      }, 3000);
    }
  </script>
</body>
</html>