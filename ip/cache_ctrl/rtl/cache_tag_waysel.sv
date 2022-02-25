`default_nettype none

module cache_tag_waysel #(
    // TODO: Specify parameter constraints
    parameter NUM_WAYS = 1,
    parameter ADDR_WIDTH = 32,
    parameter DATA_WIDTH = 32,
    parameter CLINE_SIZE_WORD = 4,
    parameter CLINE_ADDR_WIDTH = 7,
    parameter TAG_SRAM_DATA_WIDTH = 32
) (
    input wire[ADDR_WIDTH-1:0] addr_i,
    input wire[TAG_SRAM_DATA_WIDTH*NUM_WAYS-1:0] tagways_i,
    input wire[DATA_WIDTH*NUM_WAYS-1:0] dataways_i,
    output wire[DATA_WIDTH-1:0] data_o,
    output wire[NUM_WAYS-1:0] way_miss_o,
    output wire hit_o
);
    parameter TAG_OFFSET = $clog2(CLINE_SIZE_WORD) + CLINE_ADDR_WIDTH;
    parameter TAG_WIDTH = ADDR_WIDTH - TAG_OFFSET;

    wire[NUM_WAYS-1:0] way_hit;
    wire[NUM_WAYS-1:0] tag_and_data [DATA_WIDTH-1:0];

    genvar i;
    genvar j;
    generate
        for(i = 0; i < NUM_WAYS; i++) begin
            // Compare addr_i tag with tagways_i tag, then and with enable bit
            assign way_hit[i] = !(
                |(addr_i[TAG_OFFSET+:TAG_WIDTH] ^
                  tagways_i[TAG_SRAM_DATA_WIDTH*i+:TAG_WIDTH])
            ) & tagways_i[32*i+31+:1];
        end
        for(i = 0; i < DATA_WIDTH; i++) begin
            for(j = 0; j < NUM_WAYS; j++) begin
                assign tag_and_data[i][j] = dataways_i[32*j+i+:1] & way_hit[j];
            end
        end
        for(i = 0; i < DATA_WIDTH; i++) begin
            assign data_o[i] = | tag_and_data[i];
        end
    endgenerate
    
    assign hit_o = | way_hit;
    assign way_miss_o = !way_hit;
endmodule