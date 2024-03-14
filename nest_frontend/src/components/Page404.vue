<template>
    <main class=" lg:h-screen w-full flex flex-col justify-center items-center bg-white absolute -mt-[95px] overflow-hidden">
	<h1 class="text-9xl font-extrabold text-black tracking-widest">404</h1>
	<div class="bg-[#FF6A3D] px-2 text-sm rounded rotate-12 absolute">
		Page Not Found
	</div>
	<button class="mt-5">
      <a
        class="relative inline-block text-sm font-medium text-[#FF6A3D] group active:text-orange-500 focus:outline-none focus:ring"
      >

        <RouterLink to="/" class="relative inline-block px-3 py-3 font-medium group w-[250px] mt-5">
          <span class="absolute inset-0 w-full h-full transition duration-200 ease-out transform translate-x-1 translate-y-1 bg-black group-hover:-translate-x-0 group-hover:-translate-y-0"></span>
          <span class="absolute inset-0 w-full h-full bg-white border-2 border-black group-hover:bg-black"></span>
          <span class="relative text-black group-hover:text-white">Go home</span>
        </RouterLink>
      </a>
    </button>
</main>
</template>

<script>
import { RouterLink } from 'vue-router';
export default{

    components: {
        RouterLink
    }
}

</script>