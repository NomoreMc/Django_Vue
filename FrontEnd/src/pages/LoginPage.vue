<template>
  <div class="container">
    <div class="custom-card">
      <div class="img-box">
        <img
          src="https://images.unsplash.com/photo-1682685797507-d44d838b0ac7?auto=format&fit=crop&q=80&w=1470&ixlib=rb-4.0.3&ixid=M3wxMjA3fDF8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
        />
      </div>
      <div class="custom-content">
        <h2>Card 1</h2>
        <p>
          Lorem ipsum, dolor sit amet consectetur adipisicing elit. Architecto,
          hic? Magnam eum error saepe doloribus corrupti repellat quisquam alias
          doloremque!
        </p>
        <a href="">Read More</a>
      </div>
    </div>
    <div class="custom-card">
      <div class="img-box">
        <img
          src="https://images.unsplash.com/photo-1682686578023-dc680e7a3aeb?auto=format&fit=crop&q=80&w=1470&ixlib=rb-4.0.3&ixid=M3wxMjA3fDF8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
        />
      </div>
      <div class="custom-content">
        <h2>Card 2</h2>
        <p>
          Lorem ipsum, dolor sit amet consectetur adipisicing elit. Architecto,
          hic? Magnam eum error saepe doloribus corrupti repellat quisquam alias
          doloremque!
        </p>
        <a href="">Read More</a>
      </div>
    </div>
    <div class="custom-card">
      <div class="img-box">
        <img
          src="https://images.unsplash.com/photo-1682686580224-cd46ea1a6950?auto=format&fit=crop&q=80&w=1470&ixlib=rb-4.0.3&ixid=M3wxMjA3fDF8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
        />
      </div>
      <div class="custom-content">
        <h2>Card 3</h2>
        <p>
          Lorem ipsum, dolor sit amet consectetur adipisicing elit. Architecto,
          hic? Magnam eum error saepe doloribus corrupti repellat quisquam alias
          doloremque!
        </p>
        <a href="">Read More</a>
      </div>
    </div>
  </div>
</template>

<script setup>
</script>

<style scoped>
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: "Poppins", sans-serif;
}

body {
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    background: #333333;
}

.container {
    position: relative;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-wrap: wrap;
    gap: 100px 50px;
    padding: 100px 50px;
}

.container .custom-card {
    position: relative;
    display: flex;
    justify-content: center;
    align-items: flex-start;
    width: 350px;
    max-width: 100%;
    height: 300px;
    background: #FFF;
    border-radius: 20px;
    transition: 0.5s;
    box-shadow: 0 35px 80px rgba(0, 0, 0, 0.15);
}

.container .custom-card:hover {
    height: 400px;
}

.container .custom-card .img-box {
    position: absolute;
    top: 20px;
    width: 300px;
    height: 220px;
    background: #333;
    border-radius: 12px;
    overflow: hidden;
    transition: 0.5s;
}

.container .custom-card:hover .img-box {
    top: -100px;
    scale: 0.75;
    box-shadow: 0 15px 45px rgba(0, 0, 0, 0.2);
}

.container .custom-card .img-box img {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
}

.container .custom-card .custom-content {
    position: absolute;
    top: 252px;
    width: 100%;
    height: 35px;
    padding: 0 30px;
    text-align: center;
    overflow: hidden;
    transition: 0.5s;
}

.container .custom-card:hover .custom-content {
    top: 130px;
    height: 250px;
}

.container .custom-card .custom-content h2 {
    font-size: 1.5rem;
    font-weight: 700;
    color: #333333;
}

.container .custom-card .custom-content p {
    color: #333;
}

.container .custom-card .custom-content a {
    position: relative;
    top: 15px;
    display: inline-block;
    padding: 12px 25px;
    text-decoration: none;
    background: #181818;
    color: #fff;
    font-weight: 500;
}

.container .custom-card .custom-content a:hover {
    opacity: 0.8;
}

@media (max-width: 480px) {
    .container .custom-card {
        height: 320px;
        border-radius: 15px;
    }

    .container .custom-card .img-box {
        width: 185px;
        border-radius: 10px;
    }

    .container .custom-card .custom-content p {
        font-size: 0.8rem;
    }

    .container .custom-card .custom-content a {
        font-size: 0.9rem;
    }
}
</style>