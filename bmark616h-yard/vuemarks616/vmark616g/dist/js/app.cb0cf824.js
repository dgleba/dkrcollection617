(function(t){function e(e){for(var r,a,i=e[0],c=e[1],l=e[2],m=0,p=[];m<i.length;m++)a=i[m],s[a]&&p.push(s[a][0]),s[a]=0;for(r in c)Object.prototype.hasOwnProperty.call(c,r)&&(t[r]=c[r]);u&&u(e);while(p.length)p.shift()();return n.push.apply(n,l||[]),o()}function o(){for(var t,e=0;e<n.length;e++){for(var o=n[e],r=!0,i=1;i<o.length;i++){var c=o[i];0!==s[c]&&(r=!1)}r&&(n.splice(e--,1),t=a(a.s=o[0]))}return t}var r={},s={app:0},n=[];function a(e){if(r[e])return r[e].exports;var o=r[e]={i:e,l:!1,exports:{}};return t[e].call(o.exports,o,o.exports,a),o.l=!0,o.exports}a.m=t,a.c=r,a.d=function(t,e,o){a.o(t,e)||Object.defineProperty(t,e,{enumerable:!0,get:o})},a.r=function(t){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(t,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(t,"__esModule",{value:!0})},a.t=function(t,e){if(1&e&&(t=a(t)),8&e)return t;if(4&e&&"object"===typeof t&&t&&t.__esModule)return t;var o=Object.create(null);if(a.r(o),Object.defineProperty(o,"default",{enumerable:!0,value:t}),2&e&&"string"!=typeof t)for(var r in t)a.d(o,r,function(e){return t[e]}.bind(null,r));return o},a.n=function(t){var e=t&&t.__esModule?function(){return t["default"]}:function(){return t};return a.d(e,"a",e),e},a.o=function(t,e){return Object.prototype.hasOwnProperty.call(t,e)},a.p="/";var i=window["webpackJsonp"]=window["webpackJsonp"]||[],c=i.push.bind(i);i.push=e,i=i.slice();for(var l=0;l<i.length;l++)e(i[l]);var u=c;n.push([0,"chunk-vendors"]),o()})({0:function(t,e,o){t.exports=o("56d7")},"034f":function(t,e,o){"use strict";var r=o("64a9"),s=o.n(r);s.a},"56d7":function(t,e,o){"use strict";o.r(e);o("cadf"),o("551c"),o("097d");var r=o("2b0e"),s=function(){var t=this,e=t.$createElement,o=t._self._c||e;return o("div",{staticClass:"container"},[o("div",[o("router-link",{staticClass:"btn btn-primary ml-1",attrs:{to:"/marks"}},[t._v("Bmarks")]),o("router-link",{staticClass:"btn btn-primary btn-sm ml-1",attrs:{to:"/login"}},[t._v("Login")]),o("a",{staticClass:"btn btn-primary btn-sm ml-1",attrs:{href:"#"},on:{click:function(e){return e.preventDefault(),t.logout(e)}}},[t._v("Logouut")]),o("span",{staticClass:" justify-content-end ml-1"},[t._v("[ "+t._s(this.activeUsername)+" ]")])],1),o("router-view")],1)},n=[],a=(o("96cf"),o("1da1")),i={name:"app",data:function(){return{activeUser:null,jwtusername:null}},created:function(){var t=Object(a["a"])(regeneratorRuntime.mark(function t(){return regeneratorRuntime.wrap(function(t){while(1)switch(t.prev=t.next){case 0:return t.next=2,this.refreshActiveUser();case 2:case"end":return t.stop()}},t,this)}));return function(){return t.apply(this,arguments)}}(),watch:{$route:"refreshActiveUser"},methods:{login:function(){this.$router.push("/Login")},refreshActiveUser:function(){var t=Object(a["a"])(regeneratorRuntime.mark(function t(){return regeneratorRuntime.wrap(function(t){while(1)switch(t.prev=t.next){case 0:this.activeUser=localStorage.getItem("jwtToken"),this.activeUsername=localStorage.getItem("jwtusername");case 2:case"end":return t.stop()}},t,this)}));return function(){return t.apply(this,arguments)}}(),logout:function(){var t=Object(a["a"])(regeneratorRuntime.mark(function t(){return regeneratorRuntime.wrap(function(t){while(1)switch(t.prev=t.next){case 0:localStorage.removeItem("jwtToken"),localStorage.removeItem("jwtusername"),this.$router.push("/");case 3:case"end":return t.stop()}},t,this)}));return function(){return t.apply(this,arguments)}}()}},c=i,l=(o("034f"),o("2877")),u=Object(l["a"])(c,s,n,!1,null,null,null);u.options.__file="App.vue";var m=u.exports,p=(o("ab8b"),o("8c4f")),d=o("a7fe"),h=o.n(d),v=o("bc3a"),f=o.n(v),g=function(){var t=this,e=t.$createElement;t._self._c;return t._m(0)},b=[function(){var t=this,e=t.$createElement,o=t._self._c||e;return o("div",{staticClass:"row justify-content-center"},[o("div",{staticClass:"col-md-8"},[o("div",{staticClass:"card card-default"},[o("div",{staticClass:"card-header"},[t._v("Home Component")]),o("div",{staticClass:"card-body"},[t._v("\n                vmark616g  \n            ")])])])])}],k={},_=k,y=Object(l["a"])(_,g,b,!1,null,null,null);y.options.__file="HomeComponent.vue";var w=y.exports,C=function(){var t=this,e=t.$createElement,o=t._self._c||e;return o("div",[o("h1",[t._v("Create A Post")]),o("form",{on:{submit:function(e){return e.preventDefault(),t.addPost(e)}}},[o("div",{staticClass:"row"},[o("div",{staticClass:"col-md-6"},[o("div",{staticClass:"form-group"},[o("label",[t._v("Post Title:")]),o("input",{directives:[{name:"model",rawName:"v-model",value:t.post.title,expression:"post.title"}],staticClass:"form-control",attrs:{type:"text"},domProps:{value:t.post.title},on:{input:function(e){e.target.composing||t.$set(t.post,"title",e.target.value)}}})])])]),o("div",{staticClass:"row"},[o("div",{staticClass:"col-md-6"},[o("div",{staticClass:"form-group"},[o("label",[t._v("Post Body:")]),o("textarea",{directives:[{name:"model",rawName:"v-model",value:t.post.body,expression:"post.body"}],staticClass:"form-control",attrs:{rows:"5"},domProps:{value:t.post.body},on:{input:function(e){e.target.composing||t.$set(t.post,"body",e.target.value)}}})])])]),o("br"),t._m(0)])])},$=[function(){var t=this,e=t.$createElement,o=t._self._c||e;return o("div",{staticClass:"form-group"},[o("button",{staticClass:"btn btn-primary"},[t._v("Create")])])}],x={data:function(){return{post:{}}},created:function(){var t=Object(a["a"])(regeneratorRuntime.mark(function t(){return regeneratorRuntime.wrap(function(t){while(1)switch(t.prev=t.next){case 0:this.accessToken=localStorage.getItem("jwtToken"),console.log(this.accessToken),this.accessToken||this.$router.push({name:"Login"}),console.log("url=",this.$route.query.url),this.post.title=this.$route.query.title,this.post.body=this.$route.query.description;case 6:case"end":return t.stop()}},t,this)}));return function(){return t.apply(this,arguments)}}(),methods:{addPost:function(){var t=this;this.accessToken=localStorage.getItem("jwtToken");var e="".concat("https://mark616.198.144.183.160.nip.io","/blogapp/api/v1/Post/");this.axios({method:"post",url:e,data:this.post,headers:{Authorization:"Bearer ".concat(this.accessToken)}}).then(function(t){console.log(t)}).catch(function(t){console.log(t)}).then(function(){t.$router.push({name:"posts"})})}}},P=x,j=Object(l["a"])(P,C,$,!1,null,null,null);j.options.__file="CreateComponent.vue";var T=j.exports,E=function(){var t=this,e=t.$createElement,o=t._self._c||e;return o("div",[o("div",{staticClass:"row"},[t._m(0),o("div",{staticClass:"col-md-2"},[o("router-link",{staticClass:"btn btn-primary",attrs:{to:{name:"create"}}},[t._v("Create Post")])],1)]),o("br"),o("table",{staticClass:"table table-hover"},[t._m(1),o("tbody",t._l(t.posts,function(e){return o("tr",{key:e._id},[o("td",[t._v(t._s(e.title))]),o("td",[t._v(t._s(t.rmpunctuation(e.body)))]),o("td",[o("router-link",{staticClass:"btn btn-primary",attrs:{to:{name:"edit",params:{id:e.id}}}},[t._v("Edit")])],1),o("td",[o("button",{staticClass:"btn btn-danger",on:{click:function(o){o.preventDefault(),t.deletePost(e._id)}}},[t._v("Delete")])])])}))])])},R=[function(){var t=this,e=t.$createElement,o=t._self._c||e;return o("div",{staticClass:"col-md-10"},[o("h3",[t._v("Posts")])])},function(){var t=this,e=t.$createElement,o=t._self._c||e;return o("thead",[o("tr",[o("th",[t._v("Title")]),o("th",[t._v("Body")]),o("th",[t._v("Actions")])])])}],O=(o("a481"),{data:function(){return{posts:[]}},created:function(){var t=this;this.accessToken=localStorage.getItem("jwtToken");var e="".concat("https://mark616.198.144.183.160.nip.io","/blogapp/api/v1/Post/");this.axios({method:"get",url:e,headers:{Authorization:"Bearer ".concat(this.accessToken)}}).then(function(e){t.posts=e.data.results}).then(function(t){console.log(t)}).catch(function(t){console.log(t)}).then(function(){t.$router.push({name:"posts"})})},methods:{deletePost:function(t){var e=this,o="http://localhost:4000/posts/delete/".concat(t);this.axios.delete(o).then(function(o){e.posts.splice(e.posts.indexOf(t),1)})},rmpunctuation:function(t){return t.replace(/[.,/#!$%^&*;:{}=\-_`~()]/g,"")}}}),S=O,q=Object(l["a"])(S,E,R,!1,null,null,null);q.options.__file="IndexComponent.vue";var B=q.exports,L=function(){var t=this,e=t.$createElement,o=t._self._c||e;return o("div",[o("h1",[t._v("Edit Post")]),o("form",{on:{submit:function(e){return e.preventDefault(),t.updatePost(e)}}},[o("div",{staticClass:"row"},[o("div",{staticClass:"col-md-6"},[o("div",{staticClass:"form-group"},[o("label",[t._v("Post Title: ")]),o("input",{directives:[{name:"model",rawName:"v-model",value:t.post.title,expression:"post.title"}],staticClass:"form-control",attrs:{type:"text"},domProps:{value:t.post.title},on:{input:function(e){e.target.composing||t.$set(t.post,"title",e.target.value)}}})])])]),o("div",{staticClass:"row"},[o("div",{staticClass:"col-md-6"},[o("div",{staticClass:"form-group"},[o("label",[t._v("Post Body: ")]),o("textarea",{directives:[{name:"model",rawName:"v-model",value:t.post.body,expression:"post.body"}],staticClass:"form-control",attrs:{rows:"5"},domProps:{value:t.post.body},on:{input:function(e){e.target.composing||t.$set(t.post,"body",e.target.value)}}})])])]),o("br"),t._m(0)])])},U=[function(){var t=this,e=t.$createElement,o=t._self._c||e;return o("div",{staticClass:"form-group"},[o("button",{staticClass:"btn btn-primary"},[t._v("Update")])])}],A={data:function(){return{post:{}}},created:function(){var t=this,e="http://localhost:4000/posts/edit/".concat(this.$route.params.id);this.axios.get(e).then(function(e){t.post=e.data})},methods:{updatePost:function(){var t=this,e="http://localhost:4000/posts/update/".concat(this.$route.params.id);this.axios.post(e,this.post).then(function(){t.$router.push({name:"posts"})})}}},I=A,N=Object(l["a"])(I,L,U,!1,null,null,null);N.options.__file="EditComponent.vue";var D=N.exports,z=function(){var t=this,e=t.$createElement,o=t._self._c||e;return o("div",[o("div",{staticClass:"row"},[t._m(0),o("div",{staticClass:"col-md-2"},[o("router-link",{staticClass:"btn btn-success",attrs:{to:{name:"markcreate"}}},[t._v("Create")])],1)]),o("br"),o("table",{staticClass:"table table-hover"},[t._m(1),o("tbody",t._l(t.bookmks,function(e){return o("tr",{key:e.id},[o("td",[t._v(t._s(t._f("truncatepunc")(e.title,100,"")))]),o("td",[t._v(t._s(t._f("truncatepunc")(e.url,100,"")))]),o("td",[t._v(t._s(t._f("truncatepunc")(e.body,100,"")))]),o("td",[t._v(t._s(t._f("dateformat2")(e.created_at)))]),o("td",[o("router-link",{staticClass:"btn btn-primary",attrs:{to:{name:"edit",params:{id:e.id}}}},[t._v("Edit")])],1)])}))])])},M=[function(){var t=this,e=t.$createElement,o=t._self._c||e;return o("div",{staticClass:"col-md-10"},[o("h5",[t._v("Bookmks v-20")])])},function(){var t=this,e=t.$createElement,o=t._self._c||e;return o("thead",[o("tr",[o("th",[t._v("Title")]),o("th",[t._v("URL")]),o("th",[t._v("Body")]),o("th",[t._v("Created")]),o("th",[t._v("Actions")])])])}],H=o("5a0c"),J=o.n(H),W={data:function(){return{bookmks:[],nopunc:""}},created:function(){var t=this;this.accessToken=localStorage.getItem("jwtToken");var e="".concat("https://mark616.198.144.183.160.nip.io","/mark616/api/v1/bookmk/");this.axios({method:"get",url:e,headers:{Authorization:"Bearer ".concat(this.accessToken)}}).then(function(e){t.bookmks=e.data.results}).then(function(t){console.log(t)}).catch(function(t){console.log(t)}).then(function(){t.$router.push({name:"marks"})})},filters:{truncate:function(t,e,o){return t=t||".",t.substring(0,e)+o},truncateclean:function(t,e,o){return t=t||".",t=t.replace(/([.,/#+!$%^&*;:{}=\-_`~()])/g,"$1 "),t.substring(0,e)+o},truncatepunc:function(t,e,o){return t=t||".",t=t.replace(/\s*([,/.+!?:;-]+)(?!\s*$)\s*/g,"$1 "),t.substring(0,e)+o},dateformat2:function(t){if(t)return J()(String(t)).format("ddd_MMM_DD HH:mm:ss")}},methods:{deleteBookmk:function(t){var e=this,o="http://localhost:4000/marks/delete/".concat(t);this.axios.delete(o).then(function(o){e.bookmks.splice(e.bookmks.indexOf(t),1)})},rmpunctuation:function(t){return this.nopunc=t.replace(/[.,/#!$%^&*;:{}=\-_`~()]/g," "),console.log(t,this.nopunc),this.nopunc}}},V=W,K=Object(l["a"])(V,z,M,!1,null,null,null);K.options.__file="BookmkIndexComponent.vue";var F=K.exports,G=function(){var t=this,e=t.$createElement,o=t._self._c||e;return o("div",[o("h3",[t._v("Create Bookmark616")]),o("form",{on:{submit:function(e){return e.preventDefault(),t.addBookmk(e)}}},[o("div",{staticClass:"row"},[o("div",{staticClass:"col-md-6"},[o("div",{staticClass:"form-group"},[o("label",[t._v("URL:")]),o("input",{directives:[{name:"model",rawName:"v-model",value:t.bookmk.url,expression:"bookmk.url"}],staticClass:"form-control",attrs:{type:"text"},domProps:{value:t.bookmk.url},on:{input:function(e){e.target.composing||t.$set(t.bookmk,"url",e.target.value)}}})])])]),o("div",{staticClass:"row"},[o("div",{staticClass:"col-md-6"},[o("div",{staticClass:"form-group"},[o("label",[t._v("Title:")]),o("input",{directives:[{name:"model",rawName:"v-model",value:t.bookmk.title,expression:"bookmk.title"}],staticClass:"form-control",attrs:{type:"text"},domProps:{value:t.bookmk.title},on:{input:function(e){e.target.composing||t.$set(t.bookmk,"title",e.target.value)}}})])])]),o("div",{staticClass:"row"},[o("div",{staticClass:"col-md-6"},[o("div",{staticClass:"form-group"},[o("label",[t._v("Body:")]),o("textarea",{directives:[{name:"model",rawName:"v-model",value:t.bookmk.body,expression:"bookmk.body"}],staticClass:"form-control",attrs:{rows:"8"},domProps:{value:t.bookmk.body},on:{input:function(e){e.target.composing||t.$set(t.bookmk,"body",e.target.value)}}})])])]),o("br"),t._m(0)])])},Q=[function(){var t=this,e=t.$createElement,o=t._self._c||e;return o("div",{staticClass:"form-group"},[o("button",{staticClass:"btn btn-primary btn-lg"},[t._v("Create")])])}],X=(o("6b54"),{data:function(){return{bookmk:{}}},created:function(){var t=Object(a["a"])(regeneratorRuntime.mark(function t(){var e;return regeneratorRuntime.wrap(function(t){while(1)switch(t.prev=t.next){case 0:this.accessToken=localStorage.getItem("jwtToken"),console.log(this.accessToken),this.accessToken||this.$router.push({name:"Login"}),console.log("url=",this.$route.query.url),console.log("text=",this.$route.query.text),console.log("sourcei=",this.$route.query.sourcei),"pwa"===this.$route.query.sourcei?(this.bookmk.title=this.$route.query.title,this.bookmk.body=this.$route.query.description,this.bookmk.url=this.$route.query.text):(this.bookmk.title=this.$route.query.title,this.bookmk.body=this.$route.query.description,this.bookmk.url=this.$route.query.url),e=new URL(window.location.toString()),console.log("Title shared: "+e.searchParams.get("name")),console.log("Text shared: "+e.searchParams.get("description")),console.log("URL shared: "+e.searchParams.get("link")),console.log("URL shared: "+e.searchParams.get("text"));case 12:case"end":return t.stop()}},t,this)}));return function(){return t.apply(this,arguments)}}(),methods:{addBookmk:function(){var t=this;this.accessToken=localStorage.getItem("jwtToken");var e="".concat("https://mark616.198.144.183.160.nip.io","/mark616/api/v1/bookmk/");this.axios({method:"post",url:e,data:this.bookmk,headers:{Authorization:"Bearer ".concat(this.accessToken)}}).then(function(t){console.log(t)}).catch(function(t){console.log(t)}).then(function(){t.$router.push({name:"marks"})})}}}),Y=X,Z=Object(l["a"])(Y,G,Q,!1,null,null,null);Z.options.__file="BookmkCreateComponent.vue";var tt=Z.exports,et=function(){var t=this,e=t.$createElement,o=t._self._c||e;return o("div",[o("h3",[t._v("Create Bookmark616 (pwa)")]),o("form",{on:{submit:function(e){return e.preventDefault(),t.addBookmk(e)}}},[o("div",{staticClass:"row"},[o("div",{staticClass:"col-md-6"},[o("div",{staticClass:"form-group"},[o("label",[t._v("URL:")]),o("input",{directives:[{name:"model",rawName:"v-model",value:t.bookmk.url,expression:"bookmk.url"}],staticClass:"form-control",attrs:{type:"text"},domProps:{value:t.bookmk.url},on:{input:function(e){e.target.composing||t.$set(t.bookmk,"url",e.target.value)}}})])])]),o("div",{staticClass:"row"},[o("div",{staticClass:"col-md-6"},[o("div",{staticClass:"form-group"},[o("label",[t._v("Title:")]),o("input",{directives:[{name:"model",rawName:"v-model",value:t.bookmk.title,expression:"bookmk.title"}],staticClass:"form-control",attrs:{type:"text"},domProps:{value:t.bookmk.title},on:{input:function(e){e.target.composing||t.$set(t.bookmk,"title",e.target.value)}}})])])]),o("div",{staticClass:"row"},[o("div",{staticClass:"col-md-6"},[o("div",{staticClass:"form-group"},[o("label",[t._v("Body:")]),o("textarea",{directives:[{name:"model",rawName:"v-model",value:t.bookmk.body,expression:"bookmk.body"}],staticClass:"form-control",attrs:{rows:"8"},domProps:{value:t.bookmk.body},on:{input:function(e){e.target.composing||t.$set(t.bookmk,"body",e.target.value)}}})])])]),o("br"),t._m(0)])])},ot=[function(){var t=this,e=t.$createElement,o=t._self._c||e;return o("div",{staticClass:"form-group"},[o("button",{staticClass:"btn btn-primary btn-lg"},[t._v("Create")])])}],rt={data:function(){return{bookmk:{}}},created:function(){var t=Object(a["a"])(regeneratorRuntime.mark(function t(){var e;return regeneratorRuntime.wrap(function(t){while(1)switch(t.prev=t.next){case 0:this.accessToken=localStorage.getItem("jwtToken"),console.log(this.accessToken),this.accessToken||this.$router.push({name:"Login"}),console.log("url=",this.$route.query.url),console.log("text=",this.$route.query.text),console.log("sourcei=",this.$route.query.sourcei),this.$route.query.sourcei,this.bookmk.title=this.$route.query.title,this.bookmk.body=this.$route.query.description,this.bookmk.url=this.$route.query.text,e=new URL(window.location.toString()),console.log("Title shared: "+e.searchParams.get("name")),console.log("Text shared: "+e.searchParams.get("description")),console.log("URL shared: "+e.searchParams.get("link")),console.log("URL shared: "+e.searchParams.get("text"));case 12:case"end":return t.stop()}},t,this)}));return function(){return t.apply(this,arguments)}}(),methods:{addBookmk:function(){var t=this;this.accessToken=localStorage.getItem("jwtToken");var e="".concat("https://mark616.198.144.183.160.nip.io","/mark616/api/v1/bookmk/");this.axios({method:"post",url:e,data:this.bookmk,headers:{Authorization:"Bearer ".concat(this.accessToken)}}).then(function(t){console.log(t)}).catch(function(t){console.log(t)}).then(function(){t.$router.push({name:"marks"})})}}},st=rt,nt=Object(l["a"])(st,et,ot,!1,null,null,null);nt.options.__file="BookmkPwaCreateComponent.vue";var at=nt.exports,it=function(){var t=this,e=t.$createElement,o=t._self._c||e;return o("div",[o("h2",[t._v("Please Login")]),t.t_errors&&t.t_errors.length?o("ul",t._l(t.t_errors,function(e){return o("li",{key:e},[o("alert",{attrs:{show:""}},[t._v(t._s(e.message))])],1)})):t._e(),o("form",{staticClass:"form-signin"},[o("label",{staticClass:"sr-only",attrs:{for:"inputEmail"}},[t._v("User")]),o("input",{directives:[{name:"model",rawName:"v-model.trim",value:t.username,expression:"username",modifiers:{trim:!0}}],staticClass:"form-control",attrs:{type:"username",id:"inputEmail",placeholder:"user",required:"",autofocus:""},domProps:{value:t.username},on:{input:function(e){e.target.composing||(t.username=e.target.value.trim())},blur:function(e){t.$forceUpdate()}}}),o("br"),o("label",{staticClass:"sr-only",attrs:{for:"inputPassword"}},[t._v("Password")]),o("input",{directives:[{name:"model",rawName:"v-model.trim",value:t.password,expression:"password",modifiers:{trim:!0}}],staticClass:"form-control",attrs:{type:"password",id:"inputPassword",placeholder:"Password",required:""},domProps:{value:t.password},on:{input:function(e){e.target.composing||(t.password=e.target.value.trim())},blur:function(e){t.$forceUpdate()}}}),o("br"),o("button",{attrs:{type:"submit",variant:"primary"},on:{click:t.onSubmit}},[t._v("Login")]),t._v("   \n\n    "),o("br"),o("br"),o("br"),o("button",{attrs:{type:"button",variant:"success"},on:{click:function(e){e.stopPropagation(),t.register()}}},[t._v("Register")])]),o("br")])},ct=[],lt=(o("7f7f"),{name:"Login",data:function(){return{username:"",password:"",login:{},t_errors:[],state:""}},methods:{lastRouteName:function(){var t="",e=this.$router.history.stack,o=this.$router.history.index;return o>0&&(t=e[o-1].name),t},onSubmit:function(t){var e=this;t.preventDefault(),console.log(this.username),f.a.post("".concat("https://mark616.198.144.183.160.nip.io","/api/token/"),{username:this.username,password:this.password}).then(function(t){localStorage.setItem("jwtToken",t.data.access),localStorage.setItem("jwtusername",e.username),console.log(e.$router.history),e.$router.push({name:"markcreate"})}).catch(function(t){console.log(t),e.t_errors.push(t)})},register:function(){this.$router.push({name:"Register"})}}}),ut=lt,mt=Object(l["a"])(ut,it,ct,!1,null,null,null);mt.options.__file="Login.vue";var pt=mt.exports,dt=function(){var t=this,e=t.$createElement,o=t._self._c||e;return o("b-row",{staticClass:"justify-content-md-center"},[o("b-col",{attrs:{cols:"6"}},[o("h3",[t._v("Please Register")]),o("hr"),o("hr"),o("hr"),o("h2",[t._v("Register is currently not active.")]),o("hr"),o("hr"),o("hr"),t.t_errors&&t.t_errors.length?o("ul",t._l(t.t_errors,function(e){return o("li",{key:e},[o("b-alert",{attrs:{show:""}},[t._v(t._s(e.message))])],1)})):t._e(),o("b-form",{on:{submit:t.onSubmit}},[o("b-form-group",{attrs:{id:"fieldsetHorizontal",horizontal:"","label-cols":4,breakpoint:"md",label:"Enter Username"}},[o("b-form-input",{attrs:{id:"username",state:t.state},model:{value:t.register.username,callback:function(e){t.$set(t.register,"username","string"===typeof e?e.trim():e)},expression:"register.username"}})],1),o("b-form-group",{attrs:{id:"fieldsetHorizontal",horizontal:"","label-cols":4,breakpoint:"md",label:"Enter Password"}},[o("b-form-input",{attrs:{type:"password",id:"password",state:t.state},model:{value:t.register.password,callback:function(e){t.$set(t.register,"password","string"===typeof e?e.trim():e)},expression:"register.password"}})],1),o("span",[t._v(" ")]),o("span",[t._v(" ")]),o("span",[t._v(" ")]),o("b-button",{staticClass:"float-right",attrs:{type:"button",variant:"success"},on:{click:function(e){t.$router.go(-1)}}},[t._v("Cancel")])],1)],1)],1)},ht=[],vt={name:"Register",data:function(){return{register:{},t_errors:[],state:""}},methods:{onSubmit:function(t){var e=this;t.preventDefault(),f.a.post("".concat("https://mark616.198.144.183.160.nip.io","/users/sign_up.json"),this.register).then(function(t){localStorage.setItem("register_response",t.data),alert("Registered successfully"),e.$router.push({name:"Login"})}).catch(function(t){console.log(t),e.errors.push(t)})}}},ft=vt,gt=Object(l["a"])(ft,dt,ht,!1,null,null,null);gt.options.__file="Register.vue";var bt=gt.exports;r["a"].use(p["a"]),r["a"].use(h.a,f.a),r["a"].config.productionTip=!1;var kt=[{path:"/login",name:"Login",component:pt},{path:"/register",name:"Register",component:bt},{name:"home",path:"/",component:w},{name:"marks",path:"/marks",component:F,meta:{requiresAuth:!0}},{name:"markcreate",path:"/markcreate",component:tt,meta:{requiresAuth:!0}},{name:"pwamarkcreate",path:"/pwamarkcreate",component:at,meta:{requiresAuth:!0}},{name:"create",path:"/create",component:T,meta:{requiresAuth:!0}},{name:"posts",path:"/posts",component:B,meta:{requiresAuth:!0}},{name:"edit",path:"/edit/:id",component:D}];"serviceWorker"in navigator&&window.addEventListener("load",function(){navigator.serviceWorker.register("/service-worker.js").then(function(t){console.log("ServiceWorker registration successful with scope: ",t.scope)}).catch(function(t){})});var _t=new p["a"]({mode:"history",routes:kt});new r["a"](r["a"].util.extend({router:_t},m)).$mount("#app"),console.log("~20 main env"),console.log(JSON.stringify(Object({NODE_ENV:"production",VUE_APP_BACKEND_URL:"https://mark616.198.144.183.160.nip.io",BASE_URL:"/"}),null,2))},"64a9":function(t,e,o){}});
//# sourceMappingURL=app.cb0cf824.js.map