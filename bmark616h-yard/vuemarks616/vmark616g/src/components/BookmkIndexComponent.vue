<template>
  <div>
    <div class="row">
      <div class="col-md-10"><h3>Bookmks</h3></div>
      <div class="col-md-2">
        <router-link :to="{ name: 'markcreate' }" class="btn btn-primary">Create Bookmk</router-link>
      </div>
    </div>
    <br />

    <table class="table table-hover">
      <thead>
        <tr>
          <th>Title</th>
          <th>URL</th>
          <th>Body</th>
          <th>Created</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="bookmk in bookmks" :key="bookmk._id">
          <td>{{ bookmk.title }}</td>
          <td>{{ bookmk.url }}</td>
          <td>{{ bookmk.body }}</td>
          <td>{{ bookmk.created_at }}</td>
          <td><router-link :to="{ name: 'edit', params: { id: bookmk._id } }" class="btn btn-primary">Edit</router-link></td>
          <!-- <td><button class="btn btn-danger" @click.prevent="deleteBookmk(bookmk._id)">Delete</button></td> -->
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  data() {
    return {
      bookmks: [],
    };
  },
  created() {
    // get list..
    // let uri = `${process.env.VUE_APP_BACKEND_URL}/blogapp/api/v1/Bookmk/`;
    // console.log(uri);
    // this.axios.get(uri).then((response) => {
    //   this.bookmks = response.data;
    // });

    this.accessToken = localStorage.getItem("jwtToken");
    let uri = `${process.env.VUE_APP_BACKEND_URL}/mark616/api/v1/bookmk/`;
    this.axios( { method: 'get', url: uri,
        headers: {
          Authorization: `Bearer ${this.accessToken}`
        }
      }
    )
    .then((response) => {
      this.bookmks = response.data.results;
      })
    .then(function (response) {
      console.log(response);
    })
    .catch(function (error) {
      console.log(error);
    })
    .then(() => {
      this.$router.push({name: 'marks'});
    });
  },
  methods: {
    deleteBookmk(id) {
      let uri = `http://localhost:4000/marks/delete/${id}`;
      this.axios.delete(uri).then((response) => {
        this.bookmks.splice(this.bookmks.indexOf(id), 1);
      });
    },
  },
};
</script>
