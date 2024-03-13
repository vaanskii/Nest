<template>
    <div>
      <div v-if="users.length" class="flex justify-center flex-col items-center mt-5">
        <RouterLink :to="{ name: 'profile', params: { 'id': user.id } }" v-for="user in users" :key="user.id" class="flex flex-row w-[300px]  bg-gray-200 mb-5 h-[50px] items-center rounded-full hover:bg-gray-300">
          <img :src="user.get_profile_picture" class="w-8 max-h-8 ml-2 rounded-full">
          <p class="items-start flex ml-4 text-black w-[100px]">
            <strong>
              <p>{{ user.username }}</p>
            </strong>
          </p>
          <small class="ml-10">{{ user.followers_count }} Followers</small>
        </RouterLink>
      </div>
      <div v-else>
        <h1 class="text-black text-lg font-mono font-bold uppercase mt-20">User not found!</h1>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  import { RouterLink } from 'vue-router';
  
  export default {
    name: 'SearchView',
  
    data() {
      return {
        query: this.$route.query.q || '',
        users: [],
      };
    },
  
    watch: {
      $route(to, from) {
        this.query = to.query.q || '';
        this.fetchSearchResults();
      },
    },
  
    methods: {
      fetchSearchResults() {
        axios
          .post('/api/search/', { query: this.query })
          .then(response => {
            console.log('response:', response.data);
            this.users = response.data.users;
          })
          .catch(error => {
            console.log('error:', error);
          });
      },
    },
  
    mounted() {
      this.fetchSearchResults();
    },
  };
  </script>
  