for co2 in 180 400
do
    for s in 1 2
    do
        for t in def lcy
            do
                # arguments: source.nc, co2.nc, site(1,2), lfid-flag
                python plot_es_site_transient_v5.py ~/Dropbox/Documents/2018/projects/EarthShape/data/results/egu18.s${s}_${t}_${co2}ppm_lfid.nc biome_s${s}_${t}_${co2}ppm_biome.nc ../s${s}_${t}_${co2}ppm.nc $s lfid &
            done
        done
    done
wait

