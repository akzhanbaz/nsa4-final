<template>
  <header>
    <section class="section">
    <div class="container">
    </div>
    </section>
    <div class="text-box-111">
    <h1>  MOVIE </h1>
    </div>
    <div class="text-box-222">
    <p class="mt-3">© ТОО "Movie KZ", 2003-2020
      8 (7212) 910 111, 911 555
    </p>
    </div>
  </header>
</template>
<script>
export default {
  head() {
    return {
      title: "Contact"
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

.text-box-111 {
  position: absolute;
  top: 8%;
  left: 39%;
  transform: translateY(-50%);
  color: #fff;
}
.text-box-222 {
  position: absolute;
  top: 80%;
  left: 39%;
  transform: translateY(-50%);
  color: #fff;
}
.text-box-111 h1 {
  font-family: cursive;
  font-size: 1rem;
}
.text-box-222 p {
  font-size: 1rem;
  font-weight: lighter;
}

</style>
