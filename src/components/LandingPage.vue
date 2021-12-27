<template>
  <v-app >

    <NavigationDrawer/>
    <AppBar/>

    <v-main>
      <v-container class="py-8 px-6" fluid>
        <router-view/>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import NavigationDrawer from './skeleton/NavigationDrawer.vue'
import AppBar from './skeleton/AppBar.vue'
export default {
  components:{
    NavigationDrawer,
    AppBar
  },
  data: () => ({
    cards: ["Today", "Yesterday"],
    
  }),
};
</script>