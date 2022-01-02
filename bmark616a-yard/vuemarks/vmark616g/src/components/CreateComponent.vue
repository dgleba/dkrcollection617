<template>
  <div>
    <h1>Create A Post</h1>
    <form @submit.prevent="addPost">
      <div class="row">
        <div class="col-md-6">
          <div class="form-group">
            <label>Post Title:</label>
            <input type="text" class="form-control" v-model="post.title" />
          </div>
        </div>
      </div>
      <div class="row">
        <div class="col-md-6">
          <div class="form-group">
            <label>Post Body:</label>
            <textarea class="form-control" v-model="post.body" rows="5"></textarea>
          </div>
        </div>
      </div>
      <br />
      <div class="form-group">
        <button class="btn btn-primary">Create</button>
      </div>
    </form>
  </div>
</template>

<script>
import axios from 'axios'

  export default {
      data(){
      return {
        post:{}
      }
  },
  async created () {
      // this.accessToken = localStorage.getItem("jwtToken");
      // const instance = axios.create({
      //   baseURL:  `${process.env.VUE_APP_BACKEND_URL}`,
      //   timeout: 5000,
      //     headers: {
      //       Authorization: `Bearer ${this.accessToken}`
      //     }
      // });
  },
  methods: {
    addPost(){
      this.accessToken = localStorage.getItem("jwtToken");
      let uri = `${process.env.VUE_APP_BACKEND_URL}/blogapp/api/v1/Post/`;
      this.axios( { method: 'post', url: uri, data: this.post, 
          headers: {
            Authorization: `Bearer ${this.accessToken}`
          }
        }
      )
      .then(function (response) {
        console.log(response);
      })
      .catch(function (error) {
        console.log(error);
      })
      .then(() => {
        this.$router.push({name: 'posts'});
      });
    }



  }
}
</script>
