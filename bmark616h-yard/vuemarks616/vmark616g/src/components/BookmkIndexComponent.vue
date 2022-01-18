<template>
  <div>
    <div class="row">
      <div class="col-md-10"><h5>Bookmks v-23</h5></div>
      <div class="col-md-2">
        <router-link :to="{ name: 'markcreate' }" class="btn btn-success">Create</router-link>
      </div>
    </div>
    <br />

    <ul v-if="t_errors && t_errors.length">
      <li v-for="t_error of t_errors" v-bind:key="t_error">
        <!-- <alert show>{{ t_error.message }}</alert> -->
        <div class="alert alert-warning" role="alert">
            <!-- show> -->{{ t_error.message }}
        </div>
      </li>
    </ul>

    <table class="table table-hover">
      <thead>
        <tr>
          <th>Created</th>
          <th>Title</th>
          <th>URL</th>
          <th>Body</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="bookmk in bookmks" :key="bookmk.id">
          <td>{{ bookmk.created_at  | dateformat2() }}</td>
          <td>{{ bookmk.title | truncatepunc(100, '')  }}</td>
          <td>{{ bookmk.url | truncatepunc(100, '') }}</td>
          <td>{{ bookmk.body | truncatepunc(100, '')  }}</td>
          <!-- <td><router-link :to="{ name: 'edit', params: { id: bookmk.id } }" class="btn btn-primary">Edit</router-link></td> -->
          <!-- <td><button class="btn btn-danger" @click.prevent="deleteBookmk(bookmk._id)">Delete</button></td> -->
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import dayjs from "dayjs";


export default {
  data() {
    return {
      bookmks: [],
      nopunc:'',
      t_errors: [],
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
            console.log("res data resu", response.data.results);
      })
    // .then(function (response) {
    //   console.log("resp", response);
    // })
    // .catch(function (error) {
    //   console.log("terror",error);
    //   this.t_errors.push(error);
    // })
    .then((res) => {
      console.log("res=",res);
    })
    .catch((e) => {
      console.log("ee=",e);
      this.t_errors.push(e);
    })
    .then(() => {
      this.$router.push({name: 'marks'});
    });
  },

  filters: {
    // Truncate text in template.. https://stackoverflow.com/questions/35070271/vue-js-components-how-to-truncate-the-text-in-the-slot-element-in-a-component
    truncate: function(text, length, suffix) {
      text = text || "."; // ref. https://github.com/imcvampire/vue-truncate-filter/issues/10 - fails on null
      return text.substring(0, length) + suffix;
    },
    truncateclean: function(text, length, suffix) {
      text = text || "."; // ref. https://github.com/imcvampire/vue-truncate-filter/issues/10 - fails on null
      text =  text.replace(/([.,/#+!$%^&*;:{}=\-_`~()])/g,"$1 ");
      return text.substring(0, length) + suffix;
    },
    truncatepunc: function(text, length, suffix) {
      text = text || "."; // ref. https://github.com/imcvampire/vue-truncate-filter/issues/10 - fails on null
      text =  text.replace(/\s*([,=/&_~.$+!?:;-]+)(?!\s*$)\s*/g, '$1 ');
      return text.substring(0, length) + suffix;
    },
    // format date
    dateformat2: function(input) {
      if (input) {
        return dayjs(String(input)).format("ddd_MMM_DD HH:mm:ss");
      }
    }
  },

  methods: {
    // deleteBookmk(id) {
    //   let uri = `http://localhost:4000/marks/delete/${id}`;
    //   this.axios.delete(uri).then((response) => {
    //     this.bookmks.splice(this.bookmks.indexOf(id), 1);
    //   });
    // },
    
    rmpunctuation(ss) {
      this.nopunc =  ss.replace(/[.,/#!$%^&*;:{}=\-_`~()]/g," ");
      console.log(ss, this.nopunc);
      return this.nopunc;
    },
    

  },
};
</script>
