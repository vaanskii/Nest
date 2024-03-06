<template>
  <nav v-if="userStore.user.isAuthenticated && userStore.user.id">
    <form v-on:submit.prevent="submitSearch">
      <input v-model="searchQuery" type="search" placeholder="Search">
      <button type="submit">Search</button>
    </form>
    <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link> | 
    <RouterLink :to="{name: 'profile', params: {'id': userStore.user.id}}">Profile</RouterLink> |
    <a href="#" @click="logout()">Logout</a>
  </nav>
  <nav v-else>
    <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link> | 
    <router-link to="/signup">Sign up</router-link> |
    <router-link to="/login">Login</router-link>
    <Toast/>
  </nav>
  <router-view/>
</template>

<script>
import { useUserStore } from '@/store/user'
import Toast from '@/components/Toast.vue'
import { RouterLink } from 'vue-router'
import axios from 'axios'
export default{
  setup() {
    const userStore = useUserStore()
    return {
      userStore,
      searchQuery: '',
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
    },
    submitSearch() {
      if (this.searchQuery.trim() !== '') {
        this.$router.push({ name: 'search', query: { q: this.searchQuery } });
      }
    },
  },
  components: {
    Toast,
    RouterLink,
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
