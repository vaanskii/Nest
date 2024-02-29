<template>
  <nav v-if="userStore.user.isAuthenticated">
    <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link> | 
    <router-link to="#" @click="logout()">Logout</router-link>
  </nav>
  <nav v-else>
    <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link> | 
    <router-link to="/signup">Sign up</router-link> |
    <router-link to="/login">Login</router-link>
  </nav>
  <router-view/>
</template>

<script>
import { useUserStore } from '@/store/user'
import axios from 'axios'
export default{
  setup() {
    const userStore = useUserStore()
    return {
      userStore
    }
  },
  beforeCreate() {
    this.userStore.initStore()
    const token = this.userStore.user.access
    if (token) {
      axios.defaults.headers.common["Authorization"] = "Bearer " + token;
    }else {
      axios.defaults.headers.common["Authorization"] = " ";
    } 
  },
  methods: {
    logout() {
      this.userStore.removeToken()
      this.$router.push('/login')
    }
  }
}

</script>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
