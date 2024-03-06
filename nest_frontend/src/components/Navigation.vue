<template>
    <nav class="py-10 px-8 border-b border-gray-200">
      <div class="max-w-7xl mx-auto">
          <div class="flex items-center justify-between">
              <div class="menu-left flex justify-center items-center">
                  <a href="/" class="text-xl font-extrabold">NEST</a>
                    <form  v-on:submit.prevent="submitSearch" class="w-[300px] -md mx-auto ml-14" v-if="userStore.user.isAuthenticated">   
                        <div class="relative">
                            <div class="absolute inset-y-0 start-0 flex items-center ps-3 pointer-events-none">
                                <svg class="w-4 h-4 text-gray-700" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 20">
                                    <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z"/>
                                </svg>
                            </div>
                            <input v-model="searchQuery" type="search" @keydown.enter.prevent="searchOnEnter" id="default-search" class="block w-full p-2 ps-10 text-sm border rounded-2xl bg-gray-200 border-gray-100 text-gray-900 placeholder-gray-700" placeholder="Search on NEST..." required />
                        </div>
                    </form>
              </div>

              <div class="menu-center flex space-x-12 mr-96" v-if="userStore.user.isAuthenticated">
                  <RouterLink to="/" class="text-purple-700">
                      <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6 text-black">
                          <path stroke-linecap="round" stroke-linejoin="round" d="M2.25 12l8.954-8.955c.44-.439 1.152-.439 1.591 0L21.75 12M4.5 9.75v10.125c0 .621.504 1.125 1.125 1.125H9.75v-4.875c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125V21h4.125c.621 0 1.125-.504 1.125-1.125V9.75M8.25 21h8.25" />
                      </svg>
                  </RouterLink>

                  <a to="#" @click="logout()">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6 text-black">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M15.75 9V5.25A2.25 2.25 0 0 0 13.5 3h-6a2.25 2.25 0 0 0-2.25 2.25v13.5A2.25 2.25 0 0 0 7.5 21h6a2.25 2.25 0 0 0 2.25-2.25V15M12 9l-3 3m0 0 3 3m-3-3h12.75" />
                    </svg>                            
                  </a>
              </div>

              <div class="menu-right">
                <template v-if="userStore.user.isAuthenticated && userStore.user.id">
                    <RouterLink :to="{name: 'profile', params: {'id': userStore.user.id}}">{{ userStore.user.username }}</RouterLink> 
                </template>

                <template v-else>
                    <RouterLink to="/signup" class="py-3 px-6 mr-4  bg-blue-300 hover:bg-blue-500 text-white rounded-2xl">Signup</RouterLink>
                    <RouterLink to="/login" class="py-3 px-6 bg-gray-400 hover:bg-gray-600 text-white rounded-2xl">Login</RouterLink>
                </template>
              </div>
          </div>
      </div>
  </nav>
</template>

<script>
import { useUserStore } from '@/store/user'
import { RouterLink } from 'vue-router'
export default{
    setup() {
    const userStore = useUserStore()
    return {
      userStore,
      searchQuery: '',
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
    searchOnEnter(event) {
        if (!event.shiftKey) {
        event.preventDefault();
        this.submitSearch();
        }
    },
  },
  components: {
    RouterLink,
  }
}
</script>