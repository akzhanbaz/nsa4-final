<template>
  <nav class="navbar is-light">
    <div class="container">
      <div class="navbar-brand">
        <h1>QAZAQ</h1>
        <button class="button navbar-burger">
        </button>
      </div>
      <div class="navbar-menu">
        <div class="navbar-end">
          <div class="navbar-item has-dropdown is-hoverable" v-if="$auth.isAuthenticated">
            <a class="navbar-link">
              {{ $auth.loggedInUser.username }}
            </a>
            <div class="navbar-dropdown">
              <nuxt-link class="navbar-item" to="/profile">My Profile</nuxt-link>
              <hr class="navbar-divider">
              <a class="navbar-item" @click="logout">Logout</a>
            </div>
          </div>
          <template v-else>
             <nuxt-link class="btn btn-link" to="/movies">Main</nuxt-link>
             <nuxt-link class="btn btn-link" to="/About">About</nuxt-link>
            <nuxt-link class="btn btn-link" to="/Contact">Contact</nuxt-link>
            <nuxt-link class="navbar-item" to="/register">Register</nuxt-link>
            <nuxt-link class="navbar-item" to="/login">Log In</nuxt-link>
          </template>
        </div>
      </div>
    </div>
  </nav>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  computed: {
  ...mapGetters(['isAuthenticated', 'loggedInUser'])
  },
  methods: {
  async logout() {
    await this.$auth.logout();
  },
  },
}
</script>
