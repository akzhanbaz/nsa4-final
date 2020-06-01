<template>
  <header>
    <section class="section">
    <div class="container">
    </div>
    </section>
    <div class="text-box">
      <nuxt-link class="btn btn-outline btn-large btn-info" to="/movies">
        View more movie<span class="ml-2"></span>
      </nuxt-link>
      <nuxt-link class="btn btn-outline btn-large btn-info" to="/contact">
        Help with Bitcoin <span class="ml-2"></span>
      </nuxt-link>
    </div>
    <div class="text-box-99">
    <h1> DESIGNED TO MOVE </h1>
    </div>
    <div class="text-box-23">
    <p class="mt-3">Who want to watch ️ ️</p>
    </div>
  </header>
</template>
<script>
export default {
  head() {
    return {
      title: "Home page"
    };
  },
  data() {
            return {}
        }
};
</script>
<style>
header {
  min-height: 100vh;
  background-image: linear-gradient(
      to right,
      rgba(0, 0, 0, 0.5),
      rgba(0, 0, 0, 0.2)
    ),
    url("/images/panda.jpg");
  background-position: center;
  background-size: cover;
  position: relative;
}
.text-box {
  position: absolute;
  top: 90%;
  left: 38%;
  transform: translateY(-50%);
  color: #fff;
}
.text-box-99 {
  position: absolute;
  top: 58%;
  left: 15%;
  transform: translateY(-50%);
  color: #fff;
}
.text-box-23 {
  position: absolute;
  top: 76%;
  left: 39%;
  transform: translateY(-50%);
  color: #fff;
}

.text-box-99 h1 {
  font-family: cursive;
  font-size: 6rem;
}



.text-box-23 p {
  font-size: 2rem;
  font-weight: lighter;
}
</style>
