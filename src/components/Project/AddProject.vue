<template>
  <div class="text-center">
    <v-dialog v-model="dialog" width="500">
      <template v-slot:activator="{ on, attrs }">
        <v-btn
          v-bind="attrs"
          v-on="on"
          title="Add Projcet"
          color="white"
          class="text--primary"
          fab
          small
        >
          <v-icon>mdi-plus</v-icon>
        </v-btn>
      </template>

      <v-card>
        <v-card-title class="text-h5 grey lighten-2">
          Add Project
        </v-card-title>

        <v-card-text>
          <v-form ref="addprojectref">
            <v-row>
              <v-col
                ><v-text-field
                v-model="payload.name"
                  :rules="RequiredRules"
                  label="Project Name"
                ></v-text-field
              ></v-col>
            </v-row>
          </v-form>
        </v-card-text>

        <v-divider></v-divider>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="primary" text @click="addProject"> Add </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>


<script>
import { UserMixins } from "../../mixins/user";

export default {
    mixins: [UserMixins],

  data() {
    return {
      dialog: false,
      RequiredRules: [(v) => !!v || "Required"],
      payload: {
        "name": null
      }
    };
  },
  methods: {
      addProject(){
          if(this.$refs.addprojectref.validate()){
              this.POST_USER_Project(this.payload)
              .then(() => {
                this.dialog = false
                this.GET_USER_Project()
              })
          }
      }
  }
};
</script>