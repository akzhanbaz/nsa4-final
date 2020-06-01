<template>
  <main class="container my-5">
    <div class="row">
      <div class="col-12 text-center my-3">
        <h2 class="mb-3 display-4 text-uppercase">{{ movie.name }}</h2>
      </div>
      <div class="col-md-6 mb-4">
        <img v-if="!video_preview" class="video-fluid" style="width: 400px; border-radius: 10px; box-shadow: 0 1rem 1rem rgba(0,0,0,.7);"  :src="movie.video">
        <img v-else class="video-fluid" style="width: 400px; border-radius: 10px; box-shadow: 0 1rem 1rem rgba(0,0,0,.7);"  :src="video_preview">
      </div>
      <div class="col-md-4">
        <form @submit.prevent="submitMovie">
          <div class="form-group">
            <label for>Movie Name</label>
            <input type="text" class="form-control" v-model="movie.name" >
          </div>
          <div class="form-group">
            <label for>Definition</label>
            <input type="text" v-model="movie.definition" class="form-control" name="definition" >
          </div>
          <div class="form-group">
            <label for> video</label>
            <input  class="upload-video-file" accept="video/mp4,video/x-m4v,video/wmv" type="file" @change="onFileChange">
          </div>
          <div class="row">
            <div class="col-md-6">
              <div class="form-group">
                <label for>Genre</label>
                <select v-model="movie.genre" class="form-control" >
                  <option value="Easy">Easy</option>
                  <option value="Medium">Medium</option>
                  <option value="Hard">Hard</option>
                </select>
              </div>
            </div>
            <div class="col-md-6">
              <div class="form-group">
                <label for>
                  Prep time
                  <small>(minutes)</small>
                </label>
                <input type="text" v-model="movie.prep_time" class="form-control" name="definition" >
              </div>
            </div>
          </div>
          <div class="form-group mb-3">
            <label for>Country</label>
            <textarea v-model="movie.country" class="form-control" rows="8"></textarea>
          </div>
          <button type="submit" class="btn btn-success">Save</button>
        </form>
      </div>
    </div>
  </main>
</template>
<script>
export default {
  head(){
      return {
        title: "Edit movie"
      }
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
      },
      video_preview: ""
    };
  },
  methods: {
    onFileChange(e) {
      let files = e.target.files || e.dataTransfer.files;
      if (!files.length) {
        return;
      }
      this.movie.video = files[0]
      this.createImage(files[0]);
    },
    createImage(file) {
      let reader = new FileReader();
      let vm = this;
      reader.onload = e => {
        vm.video_preview = e.target.result;
      };
      reader.readAsDataURL(file);
    },
    async submitMovie() {
      let editedMovie = this.movie
      if (editedMovie.video.indexOf("http://") != -1){
        delete editedMovie["video"]
      }
      const config = {
        headers: { "content-type": "multipart/form-data" }
      };
      let formData = new FormData();
      for (let data in editedMovie) {
        formData.append(data, editedMovie[data]);
      }
      try {
        let response = await this.$axios.$patch(`/movies/${editedMovie.id}/`, formData, config);
        this.$router.push("/movies/");
      } catch (e) {
        console.log(e);
      }
    }
  }
};
</script>

<style>
</style>
