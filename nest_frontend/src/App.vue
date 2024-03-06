<template>
  <Navigation/>
  <Toast/>
  <router-view/>
</template>

<script>
import Navigation from './components/Navigation.vue'
import { useUserStore } from '@/store/user'
import Toast from '@/components/Toast.vue'
import axios from 'axios'
export default{
  setup() {
    const userStore = useUserStore()
    return {
      userStore,
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
  components: {
    Toast,
    Navigation,
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
</style>
