<template>
  <div class="container">
    <nav class="navbar navbar-expand-sm bg-dark navbar-dark">
      <ul class="navbar-nav">
        <li class="nav-item">
          <router-link to="/" class="nav-link">Home</router-link>
        </li>
        <li class="nav-item">
          <router-link to="/create" class="nav-link">Create Post</router-link>
        </li>
        <li class="nav-item">
          <router-link to="/posts" class="nav-link">Posts</router-link>
        </li>
        <!-- <li class="nav-item">
           <b-nav-item >  [ {{ this.activeUsername }} ]  </b-nav-item> 
          <b-nav-item class="ml-auto" href="#" @click.prevent="login" v-if="!activeUser">Login</b-nav-item>
        </li> -->
        <li class="nav-item">
          <router-link to="/login" class="nav-link">Login</router-link>
        </li>
        <li class="nav-item">  
          <router-link to="/logout" class="nav-link">Logout</router-link>
        </li>
        <li class="nav-item">  [ {{ this.activeUsername }} ]  </li>
      </ul>

    </nav><br />
      <router-view></router-view>
  </div>
</template>

<style>
    .fade-enter-active, .fade-leave-active {
      transition: opacity .5s
    }
    .fade-enter, .fade-leave-active {
      opacity: 0
    }
</style>

<script>
export default {
  name: 'app',
  data () {
    return {
      activeUser: null,
      jwtusername: null,
    }
  },
  async created () {
    await this.refreshActiveUser()
  },
  watch: {
    // everytime a route is changed refresh the activeUser
    '$route': 'refreshActiveUser'
  },
  methods: {
    login () {
      // this.$auth.loginRedirect()
      this.$router.push('/Login')
    },
    async refreshActiveUser () {
      // this.activeUser = await this.$auth.getUser()
      this.activeUser = localStorage.getItem("jwtToken");
      this.activeUsername = localStorage.getItem("jwtusername");
    },

    async logout () {
      // await this.$auth.logout()
      // await this.refreshActiveUser()
      localStorage.removeItem("jwtToken");
      localStorage.removeItem("jwtusername");
      this.$router.push('/')
    }
  }
}
</script>
