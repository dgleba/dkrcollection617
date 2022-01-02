<template>
  <row class="justify-content-md-center">
    <col cols="6">
      <h2>Please Login</h2>

      <ul v-if="t_errors && t_errors.length">
        <li v-for="t_error of t_errors" v-bind:key="t_error">
          <alert show>{{t_error.message}}</alert>
        </li>
      </ul>
      
      <form @submit="onSubmit">
        <form-group
          id="fieldsetHorizontalu"
          horizontal
          :label-cols="4"
          breakpoint="md"
          label="Enter Username"
        >
          <label>Username:</label>
          <input id="username" :state="state" v-model.trim="username"></form-input>
        </form-group>
        <br/>
        <form-group
          id="fieldsetHorizontalp"
          horizontal
          :label-cols="4"
          breakpoint="md"
          label="Enter Password"
        >
          <label>Password:</label>
          <input type="password" id="password" :state="state" v-model.trim="password"></form-input>
        </form-group>
        <br/>
        <button type="submit" variant="primary">Login</button> &nbsp;&nbsp; 
        <br><br><br>
        <button type="button" variant="success" @click.stop="register()">Register</button>
      </form>
        <br/>      
    </col>
  </row>
</template>

<script>
import axios from "axios";

export default {
  name: "Login",
  data() {
    return {
      username: "",
      password: "",
      login: {},
      t_errors: [],
      state: ""
    };
  },
  methods: {
    // .
    // .
    // .
    onSubmit(evt) {
      evt.preventDefault();
      axios
        .post(`${process.env.VUE_APP_BACKEND_URL}/api/token/`, { username: this.username,  password: this.password } )
        // .post(`http://10.4.1.228:3000/api/auth/login/`, this.login)
        .then(response => {
          localStorage.setItem("jwtToken", response.data.access);
          localStorage.setItem("jwtusername", this.username);
          this.$router.push({
            name: "Posts"
          });
        })
        .catch(e => {
          console.log(e);
          this.t_errors.push(e);
        });
    },
    register() {
      this.$router.push({
        name: "Register"
      });
    }
  }
};
</script>
