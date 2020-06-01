<template>
  <main class="container my-5">
    <div class="row">
      <div class="col-12 text-center my-3">
        <h2 class="mb-3 display-4 text-uppercase">{{ movie.name }}</h2>
      </div>
      <div class="col-md-6 mb-4">
        <video
          v-if="video_preview"
          class="video-fluid"
          style="width: 400px; border-radius: 10px; box-shadow: 0 1rem 1rem rgba(0,0,0,.7);"
          :src="video_preview"
          alt
        ></video>
        <video
          v-else
          class="video-fluid"
          style="width: 400px; border-radius: 10px; box-shadow: 0 1rem 1rem rgba(0,0,0,.7);"
          src="https://mdbootstrap.com/img/video/animation.mp4"
        ></video>
      </div>
      <div class="col-md-4">
        <form @submit.prevent="submitMovie">
          <div class="form-group">
            <label for>movie Name</label>
            <input type="text" class="form-control" v-model="movie.name">
          </div>
          <div class="form-group">
            <label for>Definition</label>
            <input v-model="movie.definition" type="text" class="form-control">
          </div>
          <div class="form-group">
            <label for>video</label>
            <input  class="upload-video-file" type="file" name="file" accept="video/mp4,video/x-m4v,video/wmv" @change="onFileChange">
          </div>
          <div class="row">
            <div class="col-md-6">
              <div class="form-group">
                <label for>Genre</label>
                <select v-model="movie.genre" class="form-control">
                  <option value="Cartoons">Easy</option>
                  <option value="Comedy">Medium</option>
                  <option value="romantic">Hard</option>
                </select>
              </div>
            </div>
            <div class="col-md-6">
              <div class="form-group">
                <label for>
                  Prep time
                  <small>(minutes)</small>
                </label>
                <input v-model="movie.prep_time" type="number" class="form-control">
              </div>
            </div>
          </div>
          <div class="form-group mb-3">
            <label for>Country</label>
            <textarea v-model="movie.country" class="form-control" rows="8"></textarea>
          </div>
          <button type="submit" class="btn btn-primary">Submit</button>
        </form>
      </div>
    </div>
  </main>
</template>
<script>
export default {
  head() {
    return {
      title: "Add movie"
    };
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
      this.movie.video = files[0];
      this.createImage(files[0]);
    },
    createImage(file) {
      // let image = new Image();
      let reader = new FileReader();
      let vm = this;
      reader.onload = e => {
        vm.video_preview= e.target.result;
      };
      reader.readAsDataURL(file);
    },
    async submitMovie() {
      const config = {
        headers: { "content-type": "multipart/form-data" }
      };
      let formData = new FormData();
      for (let data in this.movie) {
        formData.append(data, this.movie[data]);
      }
      try {
        let response = await this.$axios.$post("/movies/", formData, config);
        this.$router.push("/movies/");
      } catch (e) {
        console.log(e);
      }
    }
  }
};
</script>
<style scoped>
</style>
