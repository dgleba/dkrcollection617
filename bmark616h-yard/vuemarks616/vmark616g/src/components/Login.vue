<template>
  <div>
    <h2>Please Login</h2>

    <ul v-if="t_errors && t_errors.length">
      <li v-for="t_error of t_errors" v-bind:key="t_error">
        <!-- <alert show>{{ t_error.message }}</alert> -->
        <div class="alert alert-warning" role="alert"><!-- show> -->{{ t_error.message }}</div>
      </li>
    </ul>

    <form class="form-signin">
      <label for="inputEmail" class="sr-only">User</label>
      <input type="username" id="inputEmail" class="form-control" placeholder="user" required autofocus v-model.trim="username" />
      <br />
      <label for="inputPassword" class="sr-only">Password</label>
      <input type="password" id="inputPassword" class="form-control" placeholder="Password" required v-model.trim="password" />
      <br />
      <button type="submit" variant="primary" @click="onSubmit">Login</button> &nbsp;&nbsp;

      <br /><br /><br />
      <button type="button" variant="success" @click.stop="register()">Register</button>
    </form>
    <br />
    <br />
    Expires: {{ exptoken | dateformat2() }}
  </div>
</template>

<script>
import axios from "axios";
import dayjs from "dayjs";

export default {
  name: "Login",
  data() {
    return {
      username: "",
      password: "",
      login: {},
      t_errors: [],
      state: "",
      exptoken: "",
    };
  },

  methods: {
    getJWTExpireDate(jwtToken) {
      if (jwtToken) {
        let expire = "";
        try {
          const [, payload] = jwtToken.split(".");
          const { exp: expires } = JSON.parse(window.atob(payload));
          if (typeof expires === "number") {
            expire = new Date(expires * 1000);
          }
          return expire;
        } catch {
          // ignore
        }
      }
      return null;
    },
    lastRouteName: function () {
      let returnVal = "";
      const routerStack = this.$router.history.stack;
      const idx = this.$router.history.index;
      if (idx > 0) {
        returnVal = routerStack[idx - 1].name;
      }
      return returnVal;
    },

    onSubmit(evt) {
      evt.preventDefault();
      console.log(this.username);
      axios
        .post(`${process.env.VUE_APP_BACKEND_URL}/api/token/`, { username: this.username, password: this.password })
        // .post(`http://10.4.1.228:3000/api/auth/login/`, this.login)
        .then((response) => {
          localStorage.setItem("jwtToken", response.data.access);
          localStorage.setItem("jwtusername", this.username);
          console.log(this.$router.history);
          this.$router.push({
            name: "marks",
          });
        })
        .catch((e) => {
          console.log(e);
          this.t_errors.push(e);
        });
    },

    register() {
      this.$router.push({
        name: "Register",
      });
    },
  },
  filters: {
    dateformat2: function (input) {
      if (input) {
        return dayjs(String(input)).format("ddd MMM DD HH:mm");
      }
    },
  },
  created() {
    this.exptoken = this.getJWTExpireDate(localStorage.getItem("jwtToken"));
  },
};

/*

        <br/>

*/
</script>
