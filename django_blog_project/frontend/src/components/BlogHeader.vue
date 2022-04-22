<template>
  <div id="header">
    <div class="grid">
      <div></div>
      <h1>My Drf-Vue Blog</h1>
      <SearchButton />
    </div>
    <hr />
    <div class="login">
      <div v-if="hasLogin">
        <div class="dropdown">
          <button class="dropbtn">欢迎, {{ username }}!</button>
          <div class="dropdown-content">
            <router-link
              :to="{ name: 'UserCenter', params: { username: username } }"
              >用户中心</router-link
            >
            <router-link :to="{ name: 'ArticleCreate' }" v-if="isSuperuser">
              发表文章
            </router-link>
          </div>
        </div>
      </div>
      <div v-else>
        <router-link to="/login" class="login-link">登录</router-link>
      </div>
    </div>
  </div>
</template>

<script>
// eslint-disable-next-line no-unused-vars
import SearchButton from "@/components/SearchButton.vue";
import authorization from "@/utils/authorization";

export default {
  name: "BlogHeader",
  components: { SearchButton },
  data: function () {
    return {
      username: "",
      hasLogin: false,
      //isSuperuser: JSON.parse(localStorage.getItem('isSuperuser.myblog')),
      isSuperuser: localStorage.getItem('isSuperuser.myblog'),
    };
  },
  mounted() {
    // 千言万语汇成此句
    authorization().then((data) => ([this.hasLogin, this.username] = data));
  },
  methods: {
    refresh() {
      this.username = localStorage.getItem("username.myblog");
    },
  },
};
</script>

<style scoped>
.dropbtn {
  background-color: mediumslateblue;
  color: white;
  padding: 8px 8px 30px 8px;
  font-size: 16px;
  border: none;
  cursor: pointer;
  height: 16px;
  border-radius: 5px;
}
/* 容器 <div> - 需要定位下拉内容 */
.dropdown {
  position: relative;
  display: inline-block;
}
/* 下拉内容 (默认隐藏) */
.dropdown-content {
  display: none;
  position: absolute;
  background-color: #f9f9f9;
  min-width: 120px;
  box-shadow: 0 8px 16px 0 rgba(0, 0, 0, 0.2);
  text-align: center;
}
/* 下拉菜单的链接 */
.dropdown-content a {
  color: black;
  padding: 12px 16px;
  text-decoration: none;
  display: block;
}
/* 鼠标移上去后修改下拉菜单链接颜色 */
.dropdown-content a:hover {
  background-color: #f1f1f1;
}
/* 在鼠标移上去后显示下拉菜单 */
.dropdown:hover .dropdown-content {
  display: block;
}
/* 当下拉内容显示后修改下拉按钮的背景颜色 */
.dropdown:hover .dropbtn {
  background-color: darkslateblue;
}
</style>

<style scoped>
#header {
  text-align: center;
  margin-top: 20px;
}

.grid {
  display: grid;
  grid-template-columns: 1fr 4fr 1fr;
}

/* css 来源：https://blog.csdn.net/qq_39198420/article/details/77973339*/
* {
  box-sizing: border-box;
}

form {
  position: relative;
  width: 200px;
  margin: 0 auto;
}

input,
button {
  border: none;
  outline: none;
}

input {
  width: 100%;
  height: 35px;
  padding-left: 13px;
  padding-right: 46px;
}

button {
  height: 35px;
  width: 35px;
  cursor: pointer;
  position: absolute;
}

.login-link {
  color: black;
}

.login {
  text-align: right;
  padding-right: 5px;
}
</style>