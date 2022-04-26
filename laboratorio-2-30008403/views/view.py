from models.LinkedList import LinkedList

def main():
    lista_ligada = LinkedList()
    while True:
        #Pede input na Consola
        consola :str = input()
        #Faz split do input por espaco ex: comandos[0],comandos[1],comandos[2],... 
        comandos :list = consola.split(" ")
        match comandos[0].upper():
            case "RPI": # registar uma país novo.

                lista_ligada.insert_at_start(comandos[1])
                
            case "RPF": # registar país no fim.

                lista_ligada.insert_at_end(comandos[1])

            case "RPDE": # registar país depois de outro elemento já registado.

                lista_ligada.insert_after_item(comandos[2], comandos[1])
                
            case "RPAE": # regista país antes de outro elemento já registado.

                lista_ligada.insert_before_item(comandos[2], comandos[1])
                
            case "RPII": # regista país num determinado indice.

                lista_ligada.insert_at_index(int(comandos[2]), comandos[1])
                
            case "VNE": # Verifica o numero de elementos na lista.

                print("O número de elementos "+ str(lista_ligada.get_count()))   
                
            case "VP": # verifica se um país esta na lista.

                if lista_ligada.search_item(comandos[1]) == False:

                    print("O país " + str(comandos[1]) + " não se encontra na lista")
                else:
                    print("O país " + str(comandos[1]) + " encontra na lista")
                
            case "EPE": # Elimina o primeiro elemento da lista.
                print("O país " + lista_ligada.start_node.get_item() + " foi eliminado da lista")

                lista_ligada.delete_at_start()
                
            case "EUE": # Elimina o último elemento da lista.
                print ("O país " + lista_ligada.get_last_node() + " foi eliminado da lista")

                lista_ligada.delete_at_end()

            case "EP": # Elimina um páis indicado.
                if lista_ligada.search_item(comandos[1]) == False:
                    print("O país " + str(comandos[1]) + " não se encontra na lista")
                else:
                    lista_ligada.delete_element_by_value(comandos[1])
                    print("O país " + str(comandos[1]) + " foi eliminado na lista")
            
        lista_ligada.traverse_list()
            

            

