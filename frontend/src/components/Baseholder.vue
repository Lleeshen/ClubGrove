<template>
  <div v-if="hasParams()">
    <b-card no-body
      style="width: 20rem; height: 17rem""  
      class="text-center d-flex flex-column" 
      v-bind:header= "items.name"
      border-variant="dark"
      bg-variant="light">
      <b-card-body class="d-flex flex-column" 
        style="height: 8rem">
        <b-card-text class="text-left">
        <div v-if="items.description">
          Summary: {{shortenDescript()}}
        </div>
        <div v-else>
          No Description
        </div>
        <div v-if= "hasEventParams()">
          Place: {{items.place}} <br>
          Start Time: {{items.starttime}} <br>
          End Time: {{items.endtime}}
        </div>
        </b-card-text>
      </b-card-body>
      <b-card-body>
      <div v-if="!isEvent">
        <b-button v-bind:to="link" class="align-self-end mt-auto" variant="custom">To Club Page</b-button>
      </div>
      <div v-else-if= "isEvent">
      </div>
    </b-card-body>
  </b-card>
    
  </div>
</template>

<script>
// @ is an alias to /src
export default {
  name: 'Baseholder',
  props: ['items', 'isEvent'],
  data: function() {
    return {
      property: this.items
    }
  },
  methods:
  {
      hasParams: function() 
      {
          if(this.items && this.items.name)
            {
                return true;
            }
            return false;
      },
      hasEventParams: function() 
      {
          if(this.items && this.items.place
            && this.items.starttime && this.items.endtime)
            {
                return true;
            }
            return false;
      },
      shortenDescript: function ()
      {
          if(this.items.description.length > 110)
          {
            var sub=  this.items.description.substring(0,110);
            var index = sub.lastIndexOf(' ');
            return sub.substring(0,index).concat("...");
          }
          else
          {
            return this.items.description;
          }

      }

  },
  computed:
  {
      link: function()
      {
        return "club/" + encodeURI(this.items.name);
      }

  }
}

</script scoped>
.card {
  border: 2px;
}

</style>