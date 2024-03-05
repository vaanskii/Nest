<template>
    <div>
      <div v-if="users.length">
        <div v-for="user in users" :key="user.id">
          <p>
            <strong>
              <RouterLink :to="{ name: 'profile', params: { 'id': user.id } }">{{ user.username }}</RouterLink>
            </strong>
          </p>
        </div>
      </div>
      <div v-else>
        <h1>User not found!</h1>
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
      submitForm() {
        this.$router.push({ name: 'search', query: { q: this.query } });
      },
  
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
  