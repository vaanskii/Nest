<template>
    <form v-on:submit.prevent="submitForm" class="space-y-4 md:space-y-6 bg-gray-600">
        <div>
            <input type="text" v-model="form.username" placeholder="enter your username">
        </div>
        <div>
            <input type="password" v-model="form.password" placeholder="*********">
        </div>
        <button type="submit" class="p-4 bg-gray-900 rounded-lg">Login</button>

        <template v-if="errors.length > 0">
            <div class="bg-red-300 text-white rounded-lg p-6">
                <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
            </div>
        </template>
    </form>
</template>

<script>
import { useUserStore } from '@/store/user.js'
import axios from 'axios'
export default {
  setup() {
    const userStore = useUserStore()

    return {
      userStore
    }
  },
  data() {
    return {
      form: {
        username: '',
        password: ''
      },
      errors: []
    }
  },
  methods: {
    async submitForm() {
      this.errors = []

      if (this.form.username === ''){
        this.errors.push('your email is missing')
      }

      if (this.form.password === '') {
        this.errors.push('your password is missing')
      }

      if(this.errors.length === 0){
        await axios
                  .post('/api/login/', this.form)
                  .then(response => {
                      this.userStore.setToken(response.data)

                      axios.defaults.headers.common["Authorization"] = "Bearer " + response.data.access;
                  })
                  .catch(error => {
                    console.log('error', error.message)
                    this.errors.push('The username or password is incorrect')
                  })
      if (this.errors.length === 0) {
        await axios
                  .get('/api/user/')
                  .then(response => {
                    this.userStore.setUserInfo(response.data)
                    this.$router.push('/')
                  })
                  .catch(error => {
                    console.log('error', error.message)
                  })
      }
      }
    }
  }
}
</script>