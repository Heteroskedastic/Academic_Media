<template>
  <div class="mt-2">
    <v-data-table
      :loading="tableloading"
      elivation="0"
      :headers="headers"
      :items="Projects_getters"
      :items-per-page="5"
      class="elevation-1"
    >
      <template v-slot:item.action="{  item }">
        <a
          ><v-icon
            @click="$router.push('/project/'+item.id)"
            title="Preview"
            color="primary"
          >
            mdi-eye</v-icon
          >
        </a>

        
      </template>
    </v-data-table>
  </div>
</template>

<script>
import { UserMixins } from "../../mixins/user";

export default {
  mixins: [UserMixins],
  data() {
    return {
      tableloading: false,
      headers: [
        { text: "Project", value: "name" },
        { text: "Action", value: "action" },
      ],
      desserts: [
        {
          name: "Frozen Yogurt",
        },
      ],
    };
  },
  mounted() {
    this.tableloading = true
    this.GET_USER_Project()
    .then(() => {
      this.tableloading = false
    })
  },
};
</script>

<style>
</style>