<template>
        <router-view/>
</template>

<script>

export default {
  name: 'App',
   watch: {
        $route(to,) {
            document.title = to.meta.title || 'Academic Media';
        },
    },
};
</script>

<style scoped>
         body::-webkit-scrollbar {
            width: 9px;               /* width of the entire scrollbar */
          }

          body::-webkit-scrollbar-track {
            background: white;        /* color of the tracking area */
          }

          body::-webkit-scrollbar-thumb {
            background-color: #1890ff;    /* color of the scroll thumb */
            border-radius: 20px;       /* roundness of the scroll thumb */
            border: 3px solid white;  /* creates padding around scroll thumb */
          }
</style>
