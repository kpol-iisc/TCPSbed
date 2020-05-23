import transfers.rev1 as transfers
import codec.generic as codec
import algorithms.prediction.linear as edge
import time

def forward_flow_kinematic():     

    ### initialization
    obj_tx_kinematic = transfers.init_tx(kin_exit_addr, kin_exit_mode) 
    obj_rx_kinematic = transfers.init_rx(kin_entry_addr,kin_entry_mode) 
    obj_rx_haptic = transfers.init_rx(hap_entry_addr,hap_entry_mode) 
    obj_predict = edge.predict()
    
    while (1):

        print "live_ss-ei",time.time()
        
        ### receive message
	msg_kinematic = transfers.receive(obj_rx_kinematic)
	msg_haptic = transfers.receive(obj_rx_haptic)

	### decode message
	msg_kinematic_list = codec.decode(msg_kinematic) 
	msg_haptic_list = codec.decode(msg_haptic) 

	### predict kinematic command
	msg_kinematic_list = obj_predict.run(msg_kinematic_list, msg_haptic_list)
	
	### encode message
        msg_kinematic = codec.code(msg_kinematic_list)
        
	### send message
	transfers.send(obj_tx_kinematic,msg_kinematic)
 
