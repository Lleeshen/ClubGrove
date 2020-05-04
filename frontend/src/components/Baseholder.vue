<template>
  <div v-if="hasParams()">
    <b-card 
      style="width: 20rem; height: 15rem" 
      class="text-center" 
      v-bind:header= "property.name"
      border-variant="dark"
      bg-variant="light">
    <b-card-text class="text-left">
      {{shortenDescript()}}
        <div v-if= "hasEventParams()">
        Place: {{property.place}} <br>
        Start Time: {{property.starttime}} <br>
        End Time: {{property.starttime}}
        </div>
    </b-card-text>
    <div v-if= "!isEvent">
    <b-button v-bind:to="link" class="mt-auto">To club Page</b-button>
    </div>
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
          if(this.property && this.property.name
            && this.property.description)
            {
                return true;
            }
            return false;
      },
      hasEventParams: function() 
      {
          if(this.property && this.property.place
            && this.property.starttime && this.property.endtime)
            {
                return true;
            }
            return false;
      },
      shortenDescript: function ()
      {
          if(this.property.description.length > 110)
          {
            var sub=  this.property.description.substring(0,110);
            var index = sub.lastIndexOf(' ');
            return sub.substring(0,index).concat("...");
          }
          else
          {
            return this.property.description;
          }

      }

  },
  computed:
  {
      link: function()
      {
          return "club/" + this.items.name;
      }

  }
}

</script scoped>
.card {
  border: 2px;
}
</style>