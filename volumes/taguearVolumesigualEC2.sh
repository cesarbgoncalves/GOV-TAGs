#!/bin/bash
#Script criado por César Barbosa para taguear todos os volumes iguais aos da instância ao qual está conectado em 28/08/2019

#limpando a tela
tput reset

#Variáveis
regionid="us-east-1"
profile="default"
tagdata=""
instid=""

#Se não for declarada nenhuma instância como Parâmetro ($1), será usada a instância declarada na linha 9 acima.
if [ -z $1 ]
then
    instancias="$1"
fi

#Cores
RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m' # Sem Cor
ULINE='\e[4m' # Underline
NULINE='\e[0m' # Tira Underline


if [ -z ${instancias} ]
then
    printf "\n"
    echo -e ${BLUE} "Armazenando todas as Instâncias ec2 em ./instancias_sem_tag.txt ${NC}"
    #Pega todas as instâncias
    #instarr=( $(aws ec2 describe-instances --profile ${profile} --region ${regionid} --query 'Reservations[*].Instances[*].{ID:InstanceId}' --output text) )
    instarr=$(cat ./instancias_sem_tag.txt)
    printf "\n"
    echo "Lista de instâncias ec2 criada!"
else
    printf "\n"
    echo -e ${BLUE} "Iniciando varredura das TAGS na instância $1 em ${regionid} informada(s) ${NC} "
    #Pega só as instâncias informadas na variável
    instarr=${instancias}
fi

for instancia in $instarr
do
# Iniciando Levantamento de volumes e TAGS das Instâncias ##### ${instarr[@]}
    for instid in $instancia
    do
            
        echo -e "${BLUE}==============================================================================${NC}"
        printf "\n"
        instanceName=`aws ec2 describe-tags --profile ${profile} --region ${regionid} --filters "Name=resource-id,Values=${instid}" "Name=key,Values=Name" --query Tags[].{Value:Value} --output text`
        [ -z ${instanceName} ] && instanceName="sem Nome"
        echo -e "${RED} Tagueando volumes da instância ${ULINE}${instanceName^^}${NC}${NULINE} - ${instid}"
        # Iniciando o Mapeamento das TAGS para cada Instância
        for tagMap in Country Environment Owner Platform Product Service
        do
            
            if [ -z instanceName ]; then
                printf "\n"
                echo -e "${RED} Atenção! A Instância ${instid} não possui nome ${NC} "
            else
                printf "\n"
                echo -e "${RED}>>${NC} Buscando o valor da TAG ${tagMap} para a instância"
            fi
            
            tagData=`aws ec2 describe-tags --profile ${profile} --region ${regionid} --filters "Name=resource-id,Values=${instid}" "Name=key,Values=$tagMap" --query Tags[].{Value:Value} --output text`
            
            echo -e "Valor da TAG encontrado: ${BLUE} ${tagMap^^}:${tagData^^} ${NC} "
            
            echo "Localizando volumes incorporados à instância ${instanceName}"
            volidarr=( $(aws ec2 describe-volumes --profile ${profile} --region ${regionid} --filters Name=attachment.instance-id,Values=${instid} --query 'Volumes[*].Attachments[*].{volid:VolumeId}' --output text) )
            qtdVol=${#volidarr[@]}
            echo -e "Encontrado $qtdVol Volumes para a instância"
            #Iniciando o tagueamento de cada volume da instância
            for volid in ${volidarr[@]}
            do
                if [ $tagMap == Service ]; then
                    echo -e "Volume encontrado, adicionando a TAG ${BLUE} ${tagMap} ${NC} ao volume-id: ${volid}"
                    aws ec2 create-tags --profile ${profile} --region ${regionid} --resources ${volid} --tags Key="${tagMap}",Value="ec2-volume"
                    
                else
                    echo -e "Volume encontrado, adicionando a TAG ${BLUE} ${tagMap} ${NC} ao volume-id: ${volid}"
                    aws ec2 create-tags --profile ${profile} --region ${regionid} --resources ${volid} --tags Key="${tagMap}",Value="${tagData}"
                    
                fi
            done
        done
    done
done
echo -e "${BLUE}====================================================================================${NC}"
printf "\n"
