<template>
  <main class="container mt-5">
    <div class="row">
      <div class="col-12 text-right mb-4">
        <div class="d-flex justify-content-between">
          <h3>movie</h3>
          <nuxt-link to="/movies/add" class="btn btn-info">Add movie</nuxt-link>
        </div>
      </div>
      <template v-for="movie in movies">
        <div :key="movie.id" class="col-lg-3 col-md-4 col-sm-6 mb-4">
          <movie-card :onDelete="deleteMovie" :movie="movie"></movie-card>
        </div>
      </template>
    </div>
  </main>
</template>
<script>
import MovieCard from "~/components/MovieCard.vue";

export default {
  head() {
    return {
      title: "Movies list"
    };
  },
  components: {
    MovieCard
  },
  async asyncData({ $axios, params }) {
    try {
      let response = await $axios.get("/movies")
      let movies = response.data
      return { movies };
    } catch (e) {
      return { movies: [] };
    }
  },
  data() {
    return {
      movies: []
    };
  },
  methods: {
    async deleteMovie(movie_id) {
      try {
        await this.$axios.$delete(`/movies/${movie_id}/`); // delete movie
        let newMovies = await this.$axios.$get("/movies"); // get new list of movie
        this.movies = newMovies; // update list of movie
      } catch (e) {
        console.log(e);
      }
    }
  }
};
</script>
