<template>
  <main class="container my-5">
    <div class="row">
      <div class="col-12 text-center my-3">
        <h2 class="mb-3 display-4 text-uppercase">{{ movie.name }}</h2>
      </div>
      <div class="col-md-6 mb-4">
        <video
          class="video-fluid"
          style="width: 400px; border-radius: 10px; box-shadow: 0 1rem 1rem rgba(0,0,0,.7);"
          :src="movie.video"
          accept="video/mp4,video/x-m4v,video/wmv"
          alt
        ></video>
      </div>
      <div class="col-md-6">
        <div class="movie-details">
          <h4>Definition</h4>
          <p>{{ movie.definition }}</p>
          <h4>Preparation time ⏱</h4>
          <p>{{ movie.prep_time }} mins</p>
          <h4>Genre</h4>
          <p>{{ movie.genre }}</p>
          <h4>Country</h4>
          <textarea class="form-control" rows="10" v-html="movie.country" disabled />
        </div>
      </div>
    </div>
  </main>
</template>
<script>
export default {
  head() {
    return {
      title: "View movie"
    };
  },
  async asyncData({ $axios, params }) {
    try {
      let movie = await $axios.$get(`/movies/${params.id}`);
      return { movie };
    } catch (e) {
      return { movie: [] };
    }
  },
  data() {
    return {
      movie: {
        name: "",
        video: "",
        definition: "",
        genre: "",
        prep_time: null,
        country: ""
      }
    };
  }
};
</script>
<style scoped>
</style>
