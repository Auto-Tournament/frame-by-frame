# CS2's hidden commands

What Frame by Frame unhides: the 982 commands and variables CS2 keeps hidden as development-only (249 commands, 733 variables). `StripDevelopmentFlags` unhides all of them at once, not just `startmovie`. A reference for later, not a list of things we use.

**How it was made.** A throwaway dedicated server ran `cvarlist` twice: once as shipped and once with Frame by Frame loaded. This list is the difference. Each value is the server's default.

**What's missing.** It was a dedicated server, so client-only commands (most of `cl_*` and the client's renderer) aren't here, and neither is anything CS2 only registers once a map is loaded. A full list needs the same diff on the game client.

**Build.** CS2 1.41.9.2 (build 2000935), 2026-10-23. Valve adds, removes and renames these freely, so check with `find <name>` in the console before relying on one.

## Worth a look for recording

| Name | What it might give us |
|---|---|
| `demo_usefastgoto` | Faster seeking with `demo_gototick` (on by default). |
| `engine_max_ticks_to_simulate` | Caps the ticks simulated per frame when the game falls behind. |
| `host_force_frametime_to_equal_tick_interval` | Locks frame time to the tick interval. |
| `movie_fixwave` | Repairs a WAV that `startmovie` left broken after a crash. |
| `r_ssao`, `r_ssao_*` | Ambient occlusion on or off, and how strong. |
| `snd_*` | Mixer and sound settings, for the game audio in clips. |
| `tv_*` | SourceTV relay and instant-replay settings. |

## All of them

| Name | Default | Flags | Description |
|---|---|---|---|
| `+bugvoice` | *command* | norecord | Start recording bug voice attachment. |
| `Test_Checkpoint` | *command* |  | Indicate to a test script that a checkpoint has been reached |
| `Test_Loop` | *command* |  | Test_Loop <loop name> - loop back to the specified loop start point unconditionally. |
| `Test_LoopCount` | *command* |  | Test_LoopCount <loop name> <count> - loop back to the specified loop start point the specified # of times. |
| `Test_LoopForNumSeconds` | *command* |  | Test_LoopForNumSeconds <loop name> <time> - loop back to the specified start point for the specified # of seconds. |
| `Test_RandomChance` | *command* |  | Test_RandomChance <percent chance, 0-100> <token1> <token2...> - Roll the dice and maybe run the command following the percentage chance. |
| `Test_StartLoop` | *command* |  | Test_StartLoop <loop name> - Denote the start of a loop. Really just defines a named point you can jump to. |
| `Test_StartScript` | *command* |  | Start a test script running.. |
| `_resetgamestats` | *command* | sv | Erases current game stats and writes out a blank stats file |
| `addip` | *command* |  | Add an IP address to the ban list. |
| `addons` | *command* |  | list current addon info. |
| `adsp_alley_min` | 122 |  |  |
| `adsp_courtyard_min` | 126 |  |  |
| `adsp_door_height` | 112 |  |  |
| `adsp_duct_min` | 106 |  |  |
| `adsp_hall_min` | 110 |  |  |
| `adsp_low_ceiling` | 108 |  |  |
| `adsp_opencourtyard_min` | 126 |  |  |
| `adsp_openspace_min` | 130 |  |  |
| `adsp_openstreet_min` | 118 |  |  |
| `adsp_openwall_min` | 130 |  |  |
| `adsp_room_min` | 102 |  |  |
| `adsp_street_min` | 118 |  |  |
| `adsp_tunnel_min` | 114 |  |  |
| `adsp_wall_height` | 128 |  |  |
| `ai_debug_ragdoll_magnets` | false | sv |  |
| `ai_debug_speech` | 0 | sv |  |
| `ai_force_serverside_ragdoll` | false | sv |  |
| `ai_sequence_debug` | false | sv, rep |  |
| `ai_use_visibility_cache` | 1 | sv | Sets whether or not NPCs can cache their Visibility checks against other entities. If set to 2, also tests to make sure that NPC->Target results match that of Target->NPC. |
| `ai_use_visibility_cache_reciprocation` | true | sv | Sets whether or not the visibility check cache should be reciprocal. |
| `ammo_338mag_headshot_mult` | 1 | sv, rep | You must enable tweaking via tweak_ammo_impulses to use this value. |
| `ammo_338mag_impulse` | 2800 | sv, rep | You must enable tweaking via tweak_ammo_impulses to use this value. |
| `ammo_357sig_headshot_mult` | 1 | sv, rep | You must enable tweaking via tweak_ammo_impulses to use this value. |
| `ammo_357sig_impulse` | 2000 | sv, rep | You must enable tweaking via tweak_ammo_impulses to use this value. |
| `ammo_45acp_headshot_mult` | 1 | sv, rep | You must enable tweaking via tweak_ammo_impulses to use this value. |
| `ammo_45acp_impulse` | 2100 | sv, rep | You must enable tweaking via tweak_ammo_impulses to use this value. |
| `ammo_50AE_headshot_mult` | 1 | sv, rep | You must enable tweaking via tweak_ammo_impulses to use this value. |
| `ammo_50AE_impulse` | 2400 | sv, rep | You must enable tweaking via tweak_ammo_impulses to use this value. |
| `ammo_556mm_box_headshot_mult` | 1 | sv, rep | You must enable tweaking via tweak_ammo_impulses to use this value. |
| `ammo_556mm_box_impulse` | 2400 | sv, rep | You must enable tweaking via tweak_ammo_impulses to use this value. |
| `ammo_556mm_headshot_mult` | 1 | sv, rep | You must enable tweaking via tweak_ammo_impulses to use this value. |
| `ammo_556mm_impulse` | 2400 | sv, rep | You must enable tweaking via tweak_ammo_impulses to use this value. |
| `ammo_57mm_headshot_mult` | 1 | sv, rep | You must enable tweaking via tweak_ammo_impulses to use this value. |
| `ammo_57mm_impulse` | 2000 | sv, rep | You must enable tweaking via tweak_ammo_impulses to use this value. |
| `ammo_762mm_headshot_mult` | 1 | sv, rep | You must enable tweaking via tweak_ammo_impulses to use this value. |
| `ammo_762mm_impulse` | 2400 | sv, rep | You must enable tweaking via tweak_ammo_impulses to use this value. |
| `ammo_9mm_headshot_mult` | 1 | sv, rep | You must enable tweaking via tweak_ammo_impulses to use this value. |
| `ammo_9mm_impulse` | 2000 | sv, rep | You must enable tweaking via tweak_ammo_impulses to use this value. |
| `ammo_buckshot_headshot_mult` | 1 | sv, rep | You must enable tweaking via tweak_ammo_impulses to use this value. |
| `ammo_buckshot_impulse` | 600 | sv, rep | You must enable tweaking via tweak_ammo_impulses to use this value. |
| `animgraph2_enable_parallel_update` | true | sv, rep |  |
| `animgraph2_serialize_pose_recipe_in_pre_pack_entities` | true | sv, rep |  |
| `animgraph_debug_filterent` | 0 | sv, rep | Filter setting for animgraph_debug_variables output. If set to -1, show debug for all entities. If set to 0, show debug for any NPCs that have been npc_selected. If set to >0, something other than 0, show debug for the entity with the matching entindex. |
| `animgraph_debug_set_filter_params` | 0 | sv, rep | Comma separated list of params to filter against when drawing debug text overlays |
| `animgraph_debug_set_filter_tags` | 0 | sv, rep | Comma separated list of tags to filter against when drawing debug text overlays |
| `animgraph_debug_show_unreferenced_params` | false | sv, rep |  |
| `animgraph_debug_show_unreferenced_tags` | false | sv, rep |  |
| `animgraph_debug_tags` | false | sv, rep |  |
| `animgraph_debug_variables` | false | sv, rep | Turn on to see animgraph variable changes for entities passing animgraph_debug_filterent. |
| `animgraph_debug_variables_ignore_missing` | true | sv, rep | If set, animgraph_debug_variables won't show debug for warnings about sets to missing variables. |
| `animgraph_debug_variables_ignore_nonchanges` | true | sv, rep | If set, animgraph_debug_variables won't show debug for variable sets that don't change the value. |
| `animgraph_draw_traces` | false | sv, rep |  |
| `animgraph_enable_dirty_netvar_optimization` | true | rep |  |
| `animgraph_footlock_auto_ledge_detection` | true | rep | Attempt to detect when the foot is partially hanging off a ledge and stop it tilting to reach the bottom |
| `animgraph_footlock_auto_stair_detection` | true | rep | Attempt to detect when the foot is on a stair and will stop it from tilting to reach the next step |
| `animgraph_footlock_calculate_tilt` | true | rep |  |
| `animgraph_footlock_debug_foot_index` | -1 | rep |  |
| `animgraph_footlock_debug_type` | 2 | rep |  |
| `animgraph_footlock_draw_footbase` | false | rep |  |
| `animgraph_footlock_enabled` | true | rep | A master convar that effectively disables the entire footlock node. |
| `animgraph_footlock_ground_roll` | true | rep |  |
| `animgraph_footlock_hip_offset_enable` | true | rep |  |
| `animgraph_footlock_tilt_mode` | 1 | rep |  |
| `animgraph_footlock_trace_ground_enabled` | true | rep | Convar for toggling foot lock ground tracking. |
| `animgraph_footlock_use_hip_shift` | true | rep |  |
| `animgraph_footstep_node_supresses_events` | false | sv, rep |  |
| `animgraph_force_full_network_updates` | false | rep |  |
| `animgraph_ik_debug` | false | rep |  |
| `animgraph_motionmatching_print_compressionstats` | false | rep |  |
| `animgraph_slowdownonslopes_enabled` | true | rep |  |
| `animgraph_trace_ignore_prop_physics` | true | sv, rep |  |
| `animgraph_verify_dirty_netvar_optimization` | false | rep |  |
| `attached_output_stall_ms` | 250 |  |  |
| `auto_bug` | *command* | norecord | auto_bug : create non-interactive bug report. |
| `autosave` | *command* | sv | Autosave |
| `autosave_fully_async` | true | sv | Set to 1 to have autosaves execute completely on the save thread, forces 'render only' mode while the save completes |
| `autosavedangerous` | *command* | sv | AutoSaveDangerous |
| `autosavedangerousissafe` | *command* | sv |  |
| `banid` | *command* |  | Add a user ID to the ban list. |
| `banip` | *command* |  | Add an IP address to the ban list. |
| `bindtoggle` | *command* |  | Performs a bind <key> 'increment var <cvar> 0 1 1'. |
| `blink` | *command* | norecord | Blink specified convar value between two values at the specified duration. |
| `bot_force_duck` | false | sv |  |
| `bot_join_delay` | 0 | sv | Prevents bots from joining the server for this many seconds after a map change. |
| `bot_join_in_warmup` | true | sv | Prevents bots from joining the server while warmup phase is active. |
| `break_damage_inherit_scale` | 1 | sv, rep |  |
| `break_invulnerable_spawn_duration` | 0.5 | sv, rep |  |
| `breakable_force_break` | *command* | sv | Force a breakable to break |
| `breakable_multiplayer` | true | sv |  |
| `bug` | *command* | norecord | bug [auto_fill_tokens] [-title <text>] [-noscreenshot] : Activate the bug reporter. |
| `bugvoice_clear` | *command* | norecord | Clear voice attachment data. |
| `bugvoice_save` | *command* | norecord | Write buffered voice attachment data to file. |
| `check_nofilefd` | *command* |  | Print the current number of FDs reported by getrlimit |
| `cl_async_usercmd_send_recvmargin_min` | 1 |  | Min size of the recv margin queue when async usercmd send is disabled |
| `cl_cache_sendtable` | true |  | Cache sendtables |
| `cl_clockdbg` | false |  |  |
| `cl_debug_build_recvmargin_min` | 2 |  | Min size of the recv margin queue when in tools/debug mode |
| `cl_disconnect_soundevent` | StopSoundEvents.StopAllExceptMusic |  | This soundevent is called to stop the desired soundevents when the game is disconnected. |
| `cl_disconnect_voice_fade` | -1 |  | This is a fade of current voices that is called when the game is disconnected. -1.f for no fade on disconnect |
| `cl_language` | english |  | Language |
| `cl_log_tick` | false |  | Log when a tick is received |
| `cl_log_tick_skips` | 0 |  | Log when the tick delta >= this |
| `cl_parallel_readpacketentities` | true |  | Set to 1 to use threading snapshot reading (if game supports and server is sending bitcounts). |
| `cl_parallel_readpacketentities_threshold` | 2 |  | Use parallel processing of snapshot reading if above this many entries. |
| `cl_playback_screenshots` | false |  | Allows the client to playback screenshot and jpeg commands in demos. |
| `cl_precacheinfo` | *command* |  | Show precache info (client). |
| `cl_sendtable_cache_filename` | sendtables.bin |  | Send tables cache file |
| `cl_showdemooverlay` | 0 |  | How often to flash demo recording/playback overlay (0 - disable overlay, -1 - show always) |
| `cl_snd_cast_clear` | true |  |  |
| `cl_snd_cast_retrigger` | true |  |  |
| `cl_usesocketsforloopback` | false |  | When connecting to local listen server (for example, using the 'map' command), default to loopback=false, which connects to '127.0.0.1' instead of 'loopback'.  This uses the network stack so that fake lag/loss can be simulated. |
| `clear_debug_flags_on_death` | true | sv |  |
| `cloth_filter_transform_stateless` | false |  | Enable the new, stateless version of FilterTransform |
| `cloth_ground_plane_thickness` | 3 |  | Raise ground by this much for all cloth that traces the ground; should be 0 ideally |
| `cmd` | *command* |  | Forward command to server. |
| `cojob_lock_hold_warning_threshold_ms` | 10000 | sv, rep | How long in milliseconds before we warn about lock hold duration |
| `cojob_max_no_yield_time_us` | 3000 | sv, rep | Will spew if a job takes longer than the specified number of microseconds |
| `commentary_available` | false | sv | Automatically set by the game when a commentary file is available for the current map. |
| `commentary_cvarsnotchanging` | *command* | sv |  |
| `con_logfile_suffix` | 0 |  | Suffix to append to the console log, may be changed to reopen the log |
| `convars_echo_toggle_changes` | true |  | Echo to the console changes caused by toggling. |
| `cpuinfo` | *command* |  | Print CPU configuration information |
| `cq_debug` | 0 | sv, rep | Verbose command queue logging. |
| `cq_dilation_percentage` | 5 | sv, rep | When speeding up slowing down, this is how much |
| `cq_enable` | true | sv, rep | Run one usercmd per server tick and maintain a buffer.  Client speeds up/slows down it's usercmd tick rate to maintain server command queue buffering. |
| `creditsdone` | *command* | sv |  |
| `csgo_nav_jump_link_detour_threshold` | 1500 | sv, rep | don't traverse a jump link if there's a detour that costs less than this amount |
| `csm_max_num_cascades_override` | -1 |  | Number of cascades in sunlight shadow |
| `csm_max_shadow_dist_override` | -1 |  |  |
| `csm_viewmodel_shadows` | false |  |  |
| `dbghist_addline` | *command* | sv | Add a line to the debug history. Format: <category id> <line> |
| `dbghist_dump` | *command* | sv | Dump the debug history to the console. Format: <category id>     Categories:      0: Entity I/O      1: AI Decisions      2: Scene Print      3: Alyx Blind      4: Log of damage done to player   5: Player Teleport   6: Blind Zombie Sounds   7: Player Continuous |
| `debug_destructible_parts` | false | sv, rep | Draw debug information for destructible parts. |
| `debug_destructible_parts_radius_damage` | false | sv, rep |  |
| `debug_destructible_parts_ttl` | 1 | sv, rep | How long the debug draws stick around for, unless they're per-tick. |
| `debug_font_name` | Courier New |  | Debug font name |
| `debug_font_size` | 14 |  | Font size for the debug font |
| `debug_overlay_fullposition` | false | sv |  |
| `debug_physimpact` | false | sv |  |
| `debug_shared_random` | false | sv, rep |  |
| `decalfrequency` | 10 | sv, nf |  |
| `demo_allow_game_mismatch` | false |  | Allow playback of demo even if game directories are not matched [may crash or fail to load]. |
| `demo_max_consecutive_skip_packets` | 2500 |  | Don't skip more than N messages in a row when skipping in a demo file. |
| `demo_usefastgoto` | true |  | Use fast frame skipping when available for demo_goto commands. |
| `demo_writefullupdate_rate` | 60 |  | Interval time in seconds to write full updates to demo. |
| `demo_writemetafile` | *command* | norecord | save current meta file demo_<version>.meta file for use in demo upconversion. |
| `destructible_parts_destroy_parts_when_gibbing` | true | sv, rep |  |
| `dev_send_gc_message_server` | *command* | sv | <msgid> Send a blank body message with a given ID to gc for routing tests |
| `disable_priority_boost` | *command* |  | Disable focus based priority boost |
| `disable_source_soundscape_trace` | false | sv | Bypasses lookup of soundscapes for indvidual audio sources when enabled. |
| `dm_reset_spawns` | *command* | sv |  |
| `dsp_automatic` | 0 | demo |  |
| `dsp_db_min` | 80 | demo |  |
| `dsp_db_mixdrop` | 0.5 | demo |  |
| `dsp_mix_max` | 0.8 | demo |  |
| `dsp_mix_min` | 0.2 | demo |  |
| `dsp_vol_2ch` | 1 | demo |  |
| `dsp_vol_4ch` | 0.5 | demo |  |
| `dsp_vol_5ch` | 0.5 | demo |  |
| `dump_globals` | *command* | sv | Dump all global entities/states |
| `dump_loc_token` | *command* |  | List information on the given token |
| `dump_localization_files` | *command* |  | List all loaded localization files |
| `dump_response_symbols` | *command* | sv | print all response symbols to the console |
| `dumpstringtable` | *command* |  | Usage:  dumpstringtable <tablename \|all> <sv \| cl> <verbose \| simple> <element>      Print string tables to console, verbose to dump data, simple to show name and count only, can specifiy a single numeric element index to restrict spew. |
| `enable_priority_boost` | *command* |  | Disable focus based priority boost |
| `endmovie` | *command* | norecord | Stop recording movie frames. |
| `engine_accurate_input_processing_delta_time` | false |  | When true, elapsed time given to the input processing will be the time elapsed since the last input processing. This is only relevant when input is processed multiple times per frame ( i.e. multiple ticks per frame) |
| `engine_allow_multiple_simulates_per_frame` | false |  | When the client is catching up in low frame rate situations, should we run client simulate more than once a frame? |
| `engine_allow_multiple_ticks_per_frame` | true |  | When the client is catching up in low frame rate situations, should we run tick more than once a frame? |
| `engine_client_tick_pad_enable` | false |  |  |
| `engine_cpu_info_extended` | 12 CPUs (6 cores), Frequency: 3.0 GHz,  Features: F/M/S 23/49/0 AuthenticAMD 'AMD EPYC 7302 16-Core Processor                ' SSE SSE2 SSE4.1 SSE4.2 AVX AVX2 MMX RDTSC RDTSCP CMOV FCMOV PCLMULQDQ (64-bit process) |  | CPU the engine is running on. |
| `engine_frametime_amnesty_debug` | false |  | Enable logging about events that disable frame time warnings |
| `engine_frametime_print_report` | *command* |  | Print a performance report from the current data in the vprof 'lite' profiler |
| `engine_frametime_warnings_enable` | true |  | Enable framerate-related warnings, such as sv_long_frame_ms.  Disabling warnings is useful when running in situations such a debug where a slow frame rate is expected |
| `engine_max_resource_system_update_time` | 5 |  |  |
| `engine_max_ticks_to_simulate` | -1 |  | Max number of ticks to simulate per frame, after which simulation will start to slow down compared to real time. |
| `engine_no_focus_sleep_vconsole_suppress` | true |  | When VConsole is in the foreground, don't trigger engine_no_focus_sleep behavior |
| `engine_ostype` | Linux |  | OS type the engine is running on. |
| `engine_platform_name_extended` | linuxsteamrt64 |  | Platform the engine is running on. |
| `engine_render_only` | false |  |  |
| `engine_rendersystem_init` | -empty |  | Rendersystem option requested (changing this does not change the rendersystem). |
| `engine_rendersystem_shader_model` | 110 |  | Rendersystem shader model in use (changing this does not change the shader model). |
| `engine_rendersystem_used` | -empty |  | Rendersystem option in use (changing this does not change the rendersystem). |
| `engine_show_frame_ticks` | false |  |  |
| `engine_sse42` | true |  | turn on sse4.2 optimizations in the engine |
| `ent_bitvec_enable` | false | sv |  |
| `ent_cancelpendingentfires` | *command* | sv | Cancels all ent_fire created outputs that are currently waiting for their delay to expire. |
| `ent_characterize` | *command* | sv | Spew PVS debug info for entity |
| `ent_debug_draw_thinkers` | false | sv, rep |  |
| `ent_joint_axis_size` | 4 | sv |  |
| `ent_joint_only_ik_joints` | false | sv |  |
| `ent_joint_use_bind_pose` | false | sv |  |
| `ent_list_report` | *command* | sv | Reports all list of all entities in a map, one by one |
| `ent_skeleton_only_ik_joints` | false | sv |  |
| `ent_steadystate_batchsize` | 20 | sv | Max number of entities to transmit to player |
| `ent_steadystate_delay` | 5 | sv | Time in seconds without network state changes until an entity is considered for trickle updates |
| `ent_steadystate_enable` | false | sv |  |
| `ent_steadystate_interval` | 0.1 | sv | Rate at which entities can be trickled to players |
| `entity_lump_list` | *command* |  | List all known entity lumps |
| `entity_lump_spew` | *command* |  | Dump the contents of an entity lump |
| `ents` | *command* | sv | List server entities, sorted by spawn group |
| `filesystem_buffer_size` | 0 |  | Size of per file buffers. 0 for none |
| `filesystem_fake_latency` | 0 |  |  |
| `filesystem_max_stdio_read` | 16 |  |  |
| `filesystem_native` | true |  | Use native FS or STDIO |
| `filesystem_report_buffered_io` | false |  |  |
| `filesystem_unbuffered_io` | true |  |  |
| `fire_use_modifier` | false | sv, rep |  |
| `fog_volume_debug` | false | sv | If enabled, prints diagnostic information about the current fog volume |
| `footstep_audible_threshold` | 0.55 | sv, rep |  |
| `footstep_debug` | false | sv, rep |  |
| `footstep_force_volume` | -1 | sv, rep |  |
| `fp_trace` | *command* |  | Toggle field path tracing to file |
| `frag_grenade_blip_frequency` | 1 | sv, rep |  |
| `fs_async_threads` | -1 |  | Number of IO threads in async filesystem (-1 == auto) |
| `fs_clear_open_duplicate_times` | *command* |  | Clear the list of files that have been opened. |
| `fs_dump_open_duplicate_times` | *command* |  | Set fs_report_long_reads 1 before loading to use this. Prints a list of files that were opened more than once and ~how long was spent reading from them. |
| `fs_report_async_io` | false |  |  |
| `fs_report_long_reads` | 0 |  | 0:Off, 1:All (for tracking accumulated duplicate read times), >1:Microsecond threashold |
| `fs_warning_mode` | 0 |  | 0:Off, 1:Warn main thread, 2:Warn other threads |
| `func_break_reduction_factor` | 0.5 | sv |  |
| `func_breakdmg_bullet` | 0.5 | sv |  |
| `func_breakdmg_club` | 1.5 | sv |  |
| `func_breakdmg_explosive` | 1.25 | sv |  |
| `func_mover_async_movable_navmesh_updates` | true | sv |  |
| `func_mover_debug` | false | sv |  |
| `func_mover_debug_all` | false | sv |  |
| `func_mover_debug_follower` | false | sv |  |
| `func_mover_debug_parallel` | false | sv |  |
| `func_mover_debug_showtext` | false | sv |  |
| `func_mover_debug_verbose` | false | sv |  |
| `func_mover_disable_movement` | false | sv |  |
| `func_mover_force_transition_start_direction` | false | sv |  |
| `func_mover_get_speed_override` | 0 | sv |  |
| `func_mover_imgui_log_count` | 30 | sv |  |
| `func_mover_run_parallel` | true | sv |  |
| `func_rotator_debug` | false | sv |  |
| `func_rotator_run_parallel` | true | sv |  |
| `g_debug_doors` | false | sv |  |
| `g_ragdoll_important_maxcount` | 2 | sv, rep |  |
| `g_ragdoll_maxcount` | 5 | sv, rep |  |
| `gameevents_showeventlisteners` | false |  | Show listening addition/removals |
| `gameevents_showevents` | 0 |  | Dump game events to console. (1 = Show Signaling, 2 = Show Posting also). |
| `gamestats_file_output_directory` | 0 | sv | When -gamestatsfileoutputonly is specified, file will be emitted here instead of to modpath |
| `generate_null_container` | *command* | linked | Generated a nulled out container. |
| `generate_trash_synth` | *command* | linked | Args: [Asset directory Path] |
| `host_force_frametime_to_equal_tick_interval` | false |  |  |
| `host_force_max_frametime_to_tick_interval` | false |  |  |
| `ik_constraints_enabled` | true | rep |  |
| `ik_debug_all_chains_unique_color_per_chain` | false | rep |  |
| `ik_debug_ccd` | 0 | rep |  |
| `ik_debug_constraints` | -1 | rep |  |
| `ik_debug_dogleg3bone` | 0 | rep |  |
| `ik_debug_dogleg3bone_enabled` | true | rep |  |
| `ik_debug_fabrik_backwards_enabled` | true | rep |  |
| `ik_debug_fabrik_backwards_iteration_toggle` | *command* | linked |  |
| `ik_debug_fabrik_backwards_iterations` | 0 | rep |  |
| `ik_debug_fabrik_forwards_enabled` | true | rep |  |
| `ik_debug_fabrik_forwards_iteration_toggle` | *command* | linked |  |
| `ik_debug_fabrik_forwards_iterations` | 0 | rep |  |
| `ik_debug_perlin_solver` | false | sv, rep |  |
| `ik_debug_planetilt` | 0 | rep |  |
| `ik_debug_planetilt_axis_length` | 20 | rep |  |
| `ik_debug_targets` | false | rep |  |
| `ik_fabrik_align_chain` | true | rep |  |
| `ik_fabrik_backwards_enabled` | true | rep |  |
| `ik_fabrik_forwards_enabled` | true | rep |  |
| `ik_fabrik_override_num_iterations` | -1 | rep |  |
| `ik_final_fixup_enable` | true | rep |  |
| `ik_planetilt_enable` | true | rep |  |
| `imgui_cycle_undocked_window_focus` | *command* |  | Cycles focus between the game window and undocked imgui windows |
| `in_button_double_press_window` | 0.22 | sv, rep | How short the time between presses needs to be for us to consider it a double-press |
| `inferno_damage_timer` | 0.2 | sv, rep | How long between times for the inferno to deal damage. |
| `inferno_max_trace_per_tick` | 16 | sv |  |
| `instant_replay` | true |  | Enable instant replay recording. |
| `instant_replay_goto_tick` | *command* |  | Goto a direct timestamp of the replay |
| `instant_replay_goto_tick_relative` | *command* |  | Goto a direct timestamp of the replay |
| `instant_replay_history_limit` | 120 |  | Maximum amount of minutes to save history (0 is unlimited). |
| `instant_replay_live` | *command* |  | If in replay, jumps back to live |
| `instant_replay_pause` | *command* |  | Pauses instant replay. |
| `instant_replay_resume` | *command* |  | Resumes instant replay. |
| `instant_replay_skip` | *command* |  | Number of seconds to skip back to instant replay from current position |
| `instant_replay_skip_live` | *command* |  | Number of seconds to skip back to instant replay from live |
| `instant_replay_timescale` | *command* |  | Sets instant replay speed. |
| `instant_replay_togglepause` | *command* |  | Toggles instant replay. |
| `jpeg_quality` | 90 |  | Set jpeg screenshot quality. [1..100] |
| `jpeg_screenshot` | *command* |  | Take a jpeg screenshot: jpeg_screenshot [filename] [quality 1-100]. |
| `lb_barnlight_shadow_use_precomputed_vis` | true |  |  |
| `lb_bin_slices` | 8192 |  |  |
| `lb_convert_to_barn_lights_falloff_match_point` | 0.15 |  |  |
| `lb_csm_cascade_size_override` | -1 |  | Override width/height of individual cascades in the CSM |
| `lb_csm_cross_fade_override` | -1 |  | Override CSM cross fade amount |
| `lb_csm_distance_fade_override` | -1 |  | Override CSM distance fade |
| `lb_csm_draw_alpha_tested` | true |  |  |
| `lb_csm_draw_translucent` | true |  |  |
| `lb_csm_override_bulb_radius` | -1 |  | Override bulb radius for CSM |
| `lb_csm_override_staticgeo_cascades` | false |  | Override Cascades that will render static objects with lb_csm_override_staticgeo_cascades_value |
| `lb_csm_override_staticgeo_cascades_animated_verts` | true |  | If lb_csm_override_staticgeo_cascades, ensure only objects without animated verts, i.e. SCENEOBJECTFLAG_CAN_RENDER_INTO_SST flag will be excluded (as opposed to all static objects). |
| `lb_csm_override_staticgeo_cascades_value` | -1 |  | If lb_csm_override_staticgeo_cascades, override value used to determine which cascades render static objects |
| `lb_csm_receiver_plane_depth_bias` | 1.526e-05 |  | Shader depth bias applied to shadow receiver (Note this conflicts with renderstate depth bias, both now default to 0) |
| `lb_csm_receiver_plane_depth_bias_transmissive_backface` | 0.00015 |  | Depth bias applied to shadow receiver for transmissive backface geo (based on renderstate depthbias being 0) |
| `lb_cubemap_normalization_max` | 1 |  |  |
| `lb_cubemap_normalization_roughness_begin` | 0.1 |  |  |
| `lb_dynamic_shadow_penumbra` | true |  | Adjust shadow penumbra based on light size |
| `lb_dynamic_shadow_resolution` | true |  | Dynamically adjust shadow resolution |
| `lb_dynamic_shadow_resolution_base` | 1024 |  | Base resolution for dynamic shadowmap sizing.  Shadowmap size of a screen sized light |
| `lb_dynamic_shadow_resolution_delay` | 0.85 |  | Update delay for shadow size |
| `lb_dynamic_shadow_resolution_hysteresis` | 0.33 |  | Update hysteresis for shadow size |
| `lb_dynamic_shadow_resolution_quantization` | 64 |  | Quantization of dynamically computed shadow size |
| `lb_enable_binning` | true | menubar_item | SceneSystem/LightBinner/Enable Binning |
| `lb_enable_shadow_casting` | true |  | Allow stationary/dynamic lights to cast shadows. |
| `lb_shadow_texture_height_override` | -1 |  | Override height of shadow atlas texture |
| `lb_shadow_texture_width_override` | -1 |  | Override width of shadow atlas texture |
| `lb_ssss_importance_sample` | false |  |  |
| `lb_ssss_samples` | 11 |  | Subsurface sample count |
| `lb_sun_csm_size_cull_threshold_texels` | 10 |  | Size, in texels, where we will cull an object in the shadowmap |
| `lb_tile_pixels` | 8 |  |  |
| `lb_time_sliced_shadow_map_reallocation_age` | 0.7 |  | Age of cached allocation to be considered for re-allocation |
| `lb_time_sliced_shadow_map_reallocation_pct` | 0.2 |  | Likelyhood we'll re-allocate a timesliced shadowmap (to try to improve packing) |
| `lb_time_sliced_shadow_map_rendering_enable` | true |  | Allow time-sliced shadow buffer rendering when enabled via gameinfo.gi |
| `lb_timesliced_shadows_dynamic_size` | true |  |  |
| `lightbinner_precompute` | *command* |  |  |
| `lightbinner_test_computespheresilhouette` | *command* |  |  |
| `lightbinner_test_computesumsilhouette` | *command* |  |  |
| `listRecentNPCSpeech` | *command* | sv, norecord | Displays a list of the last 5 lines of speech from NPCs. |
| `listid` | *command* |  | Lists banned users. |
| `listip` | *command* |  | List IP addresses on the ban list. |
| `load` | *command* | norecord, vconsole_fuzzy | Usage:    load [save file name] |
| `loop_dump` | *command* |  | Print the listeners of the current loop mode |
| `lrucache_flush` | *command* |  | Flushes the specified cache |
| `lrucache_reset_stats` | *command* |  | Resets stats for the specified CUtlLRUCaches (or all if none specified) |
| `lrucache_set_size` | *command* |  | Sets the specified cache to the specified size |
| `lrucache_stats` | *command* |  | Spews information about all CUtlLRUCaches |
| `lservercfgfile` | listenserver.cfg | sv |  |
| `lua_assert_on_error` | false |  |  |
| `lua_report_memory` | *command* |  |  |
| `lua_shipping_assert_on_error` | false |  |  |
| `malloc_stats_dump` | *command* |  | Dump malloc stats to stderr. |
| `map_showspawnpoints` | *command* | sv | Shows player spawn points (red=invalid). Optionally pass in the duration. |
| `mapcyclefile` | mapcycle.txt | sv | Name of the .txt file used to cycle the maps on multiplayer servers |
| `markup_volume_ref_cone_angle` | 135 | sv |  |
| `mat_clearshadercache` | *command* |  | Clears the shader cache used for dynamic shader compile. |
| `mat_disable_dynamic_shader_compile` | *command* |  | Reloads all shaders from vcs files until the next time mat_reloadshaders is called |
| `mat_forcereloadshaders` | *command* |  | Force reloads all shaders (skips MD5 check). Takes optional substrings of shader names to recompile as arguments. |
| `mat_print_dead_materials` | *command* |  | Print loaded materials that have no valid layers due to not supporting any of the modes in gameinfo.gi. |
| `mat_print_error_materials` | *command* |  | Print loaded materials that are using the error shader or material. |
| `mat_print_expensive_materials` | *command* |  | Print materials sorted by cost heuristic |
| `mat_print_material_info` | *command* |  | Print info about a specific material |
| `mat_print_materials` | *command* |  | Print loaded materials. Takes an optional substring as an argument. |
| `mat_print_materials_last_frame` | *command* |  | Print materials used last frame |
| `mat_print_materials_unused` | *command* |  | Print materials that have never been used |
| `mat_print_modes` | *command* |  | Print supported rendering modes. |
| `mat_print_shader_info` | *command* |  | Print detailed info about a single shader. Takes a shader name (hero.vfx) as an argument. |
| `mat_print_shader_quality` | *command* |  | Print current shader quality setting |
| `mat_print_shaders` | *command* |  | Print loaded shaders. Takes a substring as an argument. |
| `mat_print_textures` | *command* |  | Print loaded textures in alphabetical order. Takes an optional substring as an argument. |
| `mat_print_textures_size` | *command* |  | Print loaded textures in ascending size order. Takes an optional substring as an argument. |
| `mat_print_textures_size_in_memory` | *command* |  | Print loaded textures in ascending size order as they are in memory. Takes an optional substring as an argument. |
| `mat_reinitmaterials` | *command* |  | Reinitializes all loaded materials, reloading their shaders. |
| `mat_reloadshaders` | *command* |  | Reloads all shaders. Takes optional substrings of shader names to recompile as arguments. |
| `mat_reset_material_costs` | *command* |  | Reset material cost heuristic |
| `mat_set_shader_quality` | *command* |  | Force shader quality setting (valid values are 0 or 1) |
| `mat_tonemap_debug` | 0 |  |  |
| `mem_compact` | *command* |  | Compacts the heap |
| `mem_dump` | *command* |  | Dump memory stats to text file or <stdout>. |
| `mem_test` | *command* |  |  |
| `mem_test_each_frame` | false |  | Run heap check at end of every frame |
| `mem_test_every_n_seconds` | 0 |  | Run heap check at a specified interval |
| `mem_test_quiet` | false |  | Don't print stats when memtesting |
| `memory` | *command* |  | Print memory stats. |
| `mesh_trace_data_memory_report` | *command* |  | Logs information about memory consumption by TraceDataForDraw_t/ToolsTraceData |
| `model_dump_convert_info` | *command* | sv, linked | Print model load-time conversion info |
| `mouse_disableinput` | false |  | Set to disable mouse input |
| `movie_fixwave` | *command* |  | Fixup corrupted .wav file if engine crashed during startmovie/endmovie, etc. |
| `mp_allowspectators` | true | sv, rep | toggles whether the server allows spectator mode or not |
| `mp_chattime` | 10 | sv, rep | amount of time players can chat after the game is over |
| `mp_debug_timeouts` | *command* | sv | Prints time outs to the console for debugging |
| `mp_dump_timers` | *command* | sv | Prints round timers to the console for debugging |
| `mp_fadetoblack` | false | sv, nf, rep | fade a player's screen to black when he dies |
| `mp_forcerespawn` | true | sv, nf |  |
| `mp_teamplay` | false | sv, nf |  |
| `mp_tournament` | false | sv, nf, rep |  |
| `mp_tournament_whitelist` | item_whitelist.txt | sv | Specifies the item whitelist file to use. |
| `mp_warmup_jointeam_cooldown` | 2 | sv |  |
| `mp_weaponstay` | false | sv, nf |  |
| `mp_winlimit` | 0 | sv, nf, rep | Max score one team can reach before server changes maps |
| `nav_approach_points_area_size_threshold` | 200 | sv | Ignore nav areas with at least one side smaller than this amount during approach point calculation. |
| `nav_switch` | *command* | sv | Switches to navmesh for the specified spawngroup |
| `nav_test_pos_name` | 0 | sv |  |
| `nav_test_pos_place` | -1 | sv |  |
| `net_async_clientconnect` | true |  | Enable async client connect optimization |
| `net_async_job_random_sleep` | 0 |  | Sleep randomly 0..net_async_job_random_sleep ms in the parallel server jobs; sleep is per job |
| `net_captureculldata` | *command* |  | Captures low-level data to replay path culling algorithm behavior in controlled unit test environment |
| `net_culloptimization` | true |  | Enable optimization of slow path that makes HLTV CPU consumption high in AnimGraph-using mods. Will switch to this on by default soon. |
| `net_debug_to_file` | false | sv |  |
| `net_detailed_canpacket_log` | false |  |  |
| `net_log_processing` | false |  | Log network processing |
| `net_max_message_process_count` | 0 |  | Maximum number of messages to process from a client in a single frame (0 == no limit). |
| `net_max_message_queue_size` | 0 |  | Maximum number of messages to allow waiting in queue after processing; exceeding this disconnects the client. 0 == no limit |
| `net_max_polymorphic_spew` | 5 |  | Max polymorphic variants to spew when spewing a flattened serializer. |
| `net_p2p_listen_dedicated` | false |  | Should dedicated server listen for new-style P2P? |
| `net_qospacketloss_percentage_threshold` | 5 |  | Spew a warning if packet loss percentage is above this threshold |
| `net_restrict_showmsg_socket` | 0 |  | If set, only net_showmsg spew for data inbound on this socket name e.g. client, server, etc. |
| `net_serializedentitymemory` | *command* |  | Spew CSerializedEntity memory |
| `net_serializedentitymetadatainfo` | *command* |  | Spew CSerializedEntity metadata information |
| `net_showdrop` | false |  | Show dropped packets in console |
| `net_showeventlisteners` | false | sv | Show listening addition/removals |
| `net_showevents` | 0 | sv | Dump game events to console (1=client only, 2=all). |
| `net_showmsg` | 0 |  | Show incoming message: <0\|1\|2\|name> where 1 == all and 2 == all except net_NOP |
| `net_showoob` | false |  | Show connectionless UDP traffic. |
| `net_showpeaks` | 0 |  | Show messages for large packets only: <size> |
| `net_showreliable` | 0 |  | Like net_showmsg, but only spew reliable messages |
| `net_spewcounts` | *command* |  | Spew serializer counts, client only by default, specify server to spew server counts |
| `net_stats_json` | *command* |  | Output server networking statistics in json format |
| `net_use_packet_compression` | true |  | Compress network traffic |
| `npcsolve_attract_draw` | false | sv |  |
| `npcsolve_constraint_nav` | true | sv |  |
| `npcsolve_constraint_npc` | true | sv |  |
| `npcsolve_drag_linear` | 0 | sv |  |
| `npcsolve_forward` | true | sv |  |
| `npcsolve_forward_const` | 30000 | sv |  |
| `npcsolve_forward_dist` | 200 | sv |  |
| `npcsolve_forward_margin` | 5 | sv |  |
| `npcsolve_path_close_const` | 0 | sv |  |
| `npcsolve_path_close_max_tension` | 100 | sv |  |
| `npcsolve_path_lookahead_const` | 4 | sv |  |
| `npcsolve_path_lookahead_dist` | 100 | sv |  |
| `npcsolve_path_vel_const` | 0 | sv |  |
| `npcsolve_separation` | true | sv |  |
| `npcsolve_separation_const` | 10000 | sv |  |
| `npcsolve_separation_dist` | 5 | sv |  |
| `npcsolve_separation_draw` | false | sv |  |
| `npcsolve_separation_jitter` | 0 | sv |  |
| `npcsolve_separation_r2` | false | sv |  |
| `open_asset` | *command* |  | Opens an asset in it's primary editor of choice. Specify the full path to the asset from the mod directory. |
| `p2p_listpeers` | *command* |  | List currently known peers. |
| `particle_cluster_bounds_debug` | 0 | sv, rep |  |
| `particle_cluster_debug` | 0 | sv, rep |  |
| `particle_cluster_manager_search_dist` | 256 | sv, rep |  |
| `particle_cluster_nodraw` | false | sv, rep |  |
| `particle_cluster_use_collision_hulls` | true | sv, rep |  |
| `path` | *command* |  | Show the filesystem path. |
| `path_mover_enable_high_resolution_debug_rendering` | false | sv |  |
| `path_mover_entity_spawner_debug` | false | sv |  |
| `phys_continuous_kinematic_update` | 1 | sv, rep |  |
| `phys_cull_internal_mesh_contacts` | false | rep |  |
| `phys_debug_draw` | *command* |  | Set up debug-draw of physics internal state |
| `phys_headshotscale` | 1.3 | sv, rep | Modifier for the headshot impulse hits on players |
| `phys_impactforcescale` | 1 | sv |  |
| `phys_log_updaters` | false | sv, rep |  |
| `phys_log_updaters_exclude` | weapon pistol rifle survivor common_male | sv, rep |  |
| `phys_log_updaters_include` | limbs | sv, rep |  |
| `phys_min_motion_controller_count_to_run_in_job` | 8 |  |  |
| `phys_multithreading_enabled` | true | sv, rep | Enable/Disable Multithreading in VPhysics |
| `phys_playerscale` | 10 | sv, rep | This multiplies the bullet impact impuse on players for more dramatic results when players are shot. |
| `phys_powered_ragdoll_debug` | false | sv, rep |  |
| `phys_pushscale` | 1 | sv, rep |  |
| `phys_shoot_angular_speed` | 3600 | sv |  |
| `phys_shoot_speed` | 250 | sv |  |
| `phys_show_stats` | false | sv, rep |  |
| `phys_stressbodyweights` | 5 | sv |  |
| `phys_threaded_cloth_bone_update` | false | sv, rep |  |
| `phys_threaded_kinematic_bone_update` | false | sv, rep |  |
| `phys_threaded_transform_update` | false | sv, rep |  |
| `phys_timescale` | 1 | sv | Scale time for physics |
| `phys_upimpactforcescale` | 0.375 | sv |  |
| `phys_vehicleimpactforcescale` | 1.5 | sv |  |
| `phys_visualize_awake_dynamic_only` | false | sv, rep |  |
| `phys_visualize_awake_unattached_only` | false | sv, rep |  |
| `physics_debug_entity` | *command* | sv | Dumps debug info for an entity |
| `pickup_check_period` | 0.25 | sv |  |
| `playsound` | *command* |  | playsound <soundname> |
| `playvol` | *command* |  | Play a sound at a specified volume. |
| `png_screenshot` | *command* |  | Take a .png screenshot: png_screenshot [filename] |
| `pop_var_values` | *command* |  | Restore previously pushed convars and config values |
| `population_distribution_debug` | 0 | sv, rep |  |
| `print_model_bind_pose` | *command* |  | Prints the bind pose of the specified model. Optionally limits to a particular bone and its parent chain, otherwise prints the entire skeleton. |
| `progress_enable` | *command* |  |  |
| `prop_nav_ignore_edge_len` | -1 | sv |  |
| `prop_nav_ignore_mass` | -1 | sv |  |
| `prop_nav_obstacle_avoid_mass` | 100.1 | sv |  |
| `prop_nav_obstacle_avoid_use_connection_blocker` | false | sv |  |
| `prop_nav_obstacle_block_edge_min_` | -1 | sv |  |
| `prop_nav_obstacle_block_edge_min_a` | -1 | sv |  |
| `prop_nav_obstacle_block_edge_min_c` | -1 | sv |  |
| `prop_nav_obstacle_block_mass_a` | -1 | sv |  |
| `prop_nav_obstacle_block_mass_b` | -1 | sv |  |
| `prop_nav_obstacle_block_mass_c` | -1 | sv |  |
| `props_break_max_pieces_perframe` | 16 | sv, rep | Maximum prop breakable piece count per frame (-1 = model default) |
| `push_var_values` | *command* |  | Save convars and config values |
| `r_allow_onesweep_gpusort` | true |  |  |
| `r_always_render_all_windows` | false |  | Always force all engine & tools to render |
| `r_aoproxy_cull_dist` | 12 |  | Distance to cull the AO proxy as a factor of size |
| `r_aoproxy_default_ambient_strength` | 0.2 |  |  |
| `r_aoproxy_default_light_cone_angles` | 0.3 0.3 0.3 0.3 |  |  |
| `r_aoproxy_default_light_cone_strengths` | 1 1 1 1 |  |  |
| `r_aoproxy_default_light_position_0` | 1 0 1.5 |  |  |
| `r_aoproxy_default_light_position_1` | -1 0 1.5 |  |  |
| `r_aoproxy_default_light_position_2` | 0 1 1.5 |  |  |
| `r_aoproxy_default_light_position_3` | 0 -1 1.5 |  |  |
| `r_aoproxy_min_dist` | 3 |  |  |
| `r_aoproxy_min_dist_box` | 1 |  |  |
| `r_aspectratio` | 0 |  |  |
| `r_character_decal_resolution` | 1024 |  | Resolution of character decal texture. |
| `r_decals` | 2048 | sv, rep |  |
| `r_decals_default_fade_duration` | 3 | sv, rep |  |
| `r_decals_default_start_fade` | 30 | sv, rep |  |
| `r_decals_max_triangle_anchored` | 512 | sv, rep |  |
| `r_decals_overide_fadestarttime_params` | -1 | sv, rep |  |
| `r_decals_overlap_threshold` | 6 | sv, rep |  |
| `r_decals_triangle_max_stretch` | 1.25 | sv, rep | Max stretch (and 1/x compression) ratio a triangle-anchored decal may show relative to its shape at placement. 1 = rigid follow, <= 0 = unlimited. |
| `r_directional_lightmaps` | true |  |  |
| `r_drawpixelvisibility` | false |  | Show the occlusion proxies |
| `r_experimental_lag_limiter` | false |  |  |
| `r_force_engine_render_frame` | *command* |  | Force a single render of the engine viewport. |
| `r_gpu_mem_stats` | *command* | linked | Display GPU memory usage. |
| `r_grass_allow_flattening` | false |  |  |
| `r_grass_alpha_test` | 1 |  |  |
| `r_grass_density_mode` | 1 |  | 0 = Density corresponds to blade existance, 1 = Density corresponds to blade height, 2 = Both 0 and 1 |
| `r_grass_end_fade` | 3900 |  |  |
| `r_grass_max_brightness_change` | 75 |  |  |
| `r_grass_quality` | 3 |  | 0 = Off, 1 = Low, 2 = Med, 3 = high, 4 = ultra |
| `r_grass_start_fade` | 3000 |  |  |
| `r_grass_vertex_lighting` | 0 |  |  |
| `r_hair_ao` | true |  |  |
| `r_hair_indirect_transmittance` | true |  |  |
| `r_hair_meshshader` | 0 |  |  |
| `r_hair_shadowtile` | true |  |  |
| `r_hair_wind_global_scale` | 0.3 |  |  |
| `r_hair_wind_min_noise_speed` | 20 |  |  |
| `r_hair_wind_motion_scale` | 0.07 |  |  |
| `r_hair_wind_noise` | 0.2 |  |  |
| `r_hair_wind_noise_occlusion` | 1 |  |  |
| `r_hair_wind_noise_size` | 10 |  |  |
| `r_hair_wind_occlusion` | 2 |  |  |
| `r_light_flickering_enabled` | true | sv, rep |  |
| `r_lightmap_size` | 65536 |  | Maximum lightmap resolution. |
| `r_lightmap_size_directional_irradiance` | -1 |  | Maximum lightmap resolution for directional_irradiance channel. -1 = use value of r_lightmap_size |
| `r_max_texture_pool_size` | 0 |  | Upper limit on texture pool size. |
| `r_mixed_shadows_fade_in_time` | 0.5 | sv, rep |  |
| `r_mixed_shadows_fade_out_time` | 0.5 | sv, rep |  |
| `r_print_buffers` | *command* | linked | Print Vertex/Index/GPU buffers. |
| `r_render_coordination_state` | *command* |  | Prints out the current render coordination state. |
| `r_renderdoc_auto_shader_pdbs` | true |  | Automatically generate shader debug info on capture |
| `r_renderdoc_capture_frame` | *command* | linked | Triggers a RenderDoc capture |
| `r_renderdoc_open_captures` | true |  |  |
| `r_renderdoc_show_overlay` | true |  | Show RenderDoc overlay |
| `r_renderdoc_validation_error_capture_limit` | 5 |  |  |
| `r_reset_character_decals` | false |  |  |
| `r_skip_precache_validation_check` | true |  |  |
| `r_ssao` | true |  | Set to use screen-space ambient occlusion |
| `r_ssao_bias` | 2.5 |  |  |
| `r_ssao_blur` | true |  |  |
| `r_ssao_radius` | 8 |  |  |
| `r_ssao_strength` | 3 |  |  |
| `r_texture_hookup_uses_threadpool` | true |  | Async Texture hookup uses its own threadpool instead of the global pool. |
| `r_texture_nonstreaming_load` | true |  | Allow immediately loading mips of textures (when possible) when their headers are loaded, saving IO & reducing latency. |
| `r_texture_pool_size` | 1600 |  | Total size of the texture pool in MB |
| `r_texture_stream_max_resolution` | 2147483647 |  | Maximum resolution for top mip level in streaming textures |
| `r_texture_stream_mip_bias` | 0 |  | Biases the mip level the texture streaming system choses to stream for each texture. |
| `r_texturefilteringquality` | 1 |  | 0: Bilinear, 1: Trilinear, 2: Aniso 2x, 3: Aniso 4x, 4: Aniso 8x, 5: Aniso 16x |
| `r_textures_evict_all` | *command* | linked | Evict all resident texture. |
| `r_toggleviewportsize` | *command* |  | Toggles viewport size between small + full window. |
| `r_ui_update_parallel_with_server` | false |  |  |
| `r_validate_texture_streaming` | false |  | Dumps state of texture streaming at the next frame boundary. |
| `r_vconsole_foregroundforcerender` | true |  | When VConsole is in the foreground, force all engine & tools to render |
| `r_viewport` | *command* |  | Slams viewport size to a specified value. |
| `r_wait_on_present` | false |  |  |
| `r_world_frame_load_threshold_ms` | 10 |  |  |
| `r_world_wind_dir` | 0.707 0.707 0 |  |  |
| `r_world_wind_frequency_grass` | 0.03 |  |  |
| `r_world_wind_frequency_trees` | 0.003 |  |  |
| `r_world_wind_offset_speed` | 0.25 0.3 0.2 |  |  |
| `r_world_wind_smooth_time` | 2 |  |  |
| `r_world_wind_strength` | 40 |  |  |
| `ragdoll_debug_item_detachment` | false | sv, rep |  |
| `ragdoll_override_root_orientation` | true | sv, rep |  |
| `ragdoll_parallel_pose_control` | false | sv, rep |  |
| `ragdoll_prop_settle` | true | sv, rep | Enable more aggressive ragdoll settling |
| `ragdoll_prop_sleepaftertime` | 4 | sv, rep | After this many seconds of being basically stationary, the ragdoll will go to sleep. |
| `ragdoll_prop_sleepdisabletime` | 1.5 | sv, rep | Ragdoll is not allowed to physically sleep until this timer has elapsed. |
| `ragdoll_scale_sleep_tolerance` | true | sv, rep |  |
| `ragdoll_visualize_creation_skeleton` | false | sv, rep |  |
| `ragdoll_vphysics_scale` | 0.5 | sv, rep | How much we scale physics impacts against the ragdoll. |
| `ray_bench` | *command* | sv | Load the rays and run the benchmark |
| `reload_model` | *command* |  | Force a reload of a vmdl resource |
| `removeid` | *command* |  | Remove a user ID from the ban list. |
| `removeip` | *command* |  | Remove an IP address from the ban list. |
| `report_soundpatch` | *command* | sv | reports sound patch count |
| `resource_leaks` | *command* |  | resource_leaks <resource_name>: Show resource leaks for the named resource |
| `resource_list` | *command* |  | List loaded resources matching a substring |
| `resource_log_allocate_timing` | *command* |  | Log time spent in Allocate for all resource types |
| `resource_repeated_reload` | *command* |  | resource_repeated_reload <count> <resource_name> (<resource name> ...): Load and unload the specified resource(s) |
| `resource_reset_allocate_timing` | *command* |  | Reset tracked time spent in Allocate (see resource_log_allocate_timing) |
| `rr_debugclassname` | 0 | sv, rep | If set, rr_debugclassname will print only response tests where 'classname' corresponds to this variable. Use to filter for a specific character. |
| `rr_debugresponseconcept` | 0 | sv, rep | If set, rr_debugresponseconcept will print only responses testing for the specified concept |
| `rr_debugresponses` | 0 | sv, rep | Show verbose matching output (1 for simple, 2 for rule scoring, 3 for noisy). If set to 4, it will only show response success/failure for npc_selected NPCs. |
| `rr_debugrule` | 0 | sv, rep | If set to the name of the rule, that rule's score will be shown whenever a concept is passed into the response rules system. |
| `rtx_dynamic_blas` | true |  | Allow dynamic BLAS creation for geometry going through the compute shader skinning path. |
| `rtx_dynamic_blas_caching` | true |  | Cache dynamic BLAS if geometry has not changed |
| `rtx_force_default_hitgroup` | false |  | Forces all ray traced geometry to use default hit shaders instead of specialized ones. |
| `rtx_texture_resolution` | 512 |  | Sets the texture resolution the raytracer will mark to stream in |
| `save` | *command* | sv, norecord | Save Game |
| `save_async` | true | sv |  |
| `save_clear_subdirectory` | *command* | sv, rep |  |
| `save_debug_snapshots` | true | sv, rep | Save/Load debug snapshot data |
| `save_fake_hitch` | 0 | sv | Force a busy wait for the specified number of milliseconds during save to simulate a hitch |
| `save_finish_async` | *command* | sv |  |
| `save_history_count` | 1 | sv | Keep this many old copies in history of autosaves and quicksaves. |
| `save_parallel` | true | sv, rep |  |
| `save_screenshot` | 2 | sv | 0 = none, 1 = non-autosave, 2 = always, 3 = bug_only |
| `save_set_subdirectory` | *command* | sv, rep |  |
| `save_showelapsedtime` | *command* | sv | display up-to-date elapsed play time |
| `save_spew` | false | sv, rep |  |
| `save_watchclass` | *command* | sv | Restrict spew to entities with matching classname |
| `save_watchentity` | *command* | sv | Restrict spew to entity index |
| `save_write_kv3` | false | sv, rep | Write the KV3 entity data as a text file in the save directory |
| `sc_aggregate_gpu_culling` | true |  | Toggles GPU culling of aggregate meshes |
| `sc_aggregate_gpu_occlusion_culling` | true |  |  |
| `sc_allow_dithered_lod` | true |  | Allow use of dithered lod transitions |
| `sc_allow_dynamic_constant_batching` | true |  |  |
| `sc_allow_precomputed_vismembers` | true |  |  |
| `sc_allow_write_depth_before_blend` | true |  |  |
| `sc_barnlight_enable_precomputed_vis` | true |  | Enable use of precomputed vis membership for lights (requires map restart) |
| `sc_batch_layer_cb_updates` | true |  |  |
| `sc_cache_envmap_lpv_lookup` | true |  |  |
| `sc_clutter_density_full_size` | 0.0075 |  | Screen-size where clutter will be full density |
| `sc_clutter_density_none_size` | 0.0035 |  | Screen-size where clutter will be gone |
| `sc_disable_baked_lighting` | false |  |  |
| `sc_distancefield_visualize_atlas` | false |  |  |
| `sc_dithered_lod_transition_amt` | 0.075 |  | Percentage of the transition between two lods we will apply a dither |
| `sc_enable_discard` | true |  |  |
| `sc_force_single_display_list_per_layer` | false |  |  |
| `sc_hdr_enabled_override` | -1 |  | Override default setting for HDR rendering. -1 default, 0 NoHdr, 1 Hdr, 2 Hdr 1010102 3 Hdr 111110 |
| `sc_instanced_mesh_gpu_culling` | true |  | Toggles GPU culling of instanced meshes |
| `sc_instanced_mesh_gpu_density_culling` | true |  | Toggles density culling (if enabled) |
| `sc_instanced_mesh_gpu_occlusion_culling` | true |  | Toggles GPU occlusion of instanced meshes |
| `sc_instanced_mesh_gpu_vis_culling` | true |  | Toggles GPU vis of instanced meshes |
| `sc_instanced_mesh_lod_bias` | 1.25 |  | Bias for LOD selection of instanced meshes |
| `sc_instanced_mesh_lod_bias_shadow` | 1.75 |  | Bias for LOD selection of instanced meshes in shadowmaps |
| `sc_instanced_mesh_motion_vectors` | true |  | Toggles motion vector support for instanced meshes |
| `sc_instanced_mesh_opaque_fade` | true |  | Toggles fade support for instanced meshes |
| `sc_instanced_mesh_shadows_batch_across_materials` | false |  | Toggles whether mesh shader instanced can batch on reflectivity |
| `sc_instanced_mesh_size_cull_bias` | 1.5 |  | Bias for size culling of instanced meshes |
| `sc_instanced_mesh_size_cull_bias_shadow` | 2 |  | Bias for size culling instanced meshes in shadowmaps |
| `sc_keep_all_layers` | false |  |  |
| `sc_layer_batch_threshold` | 128 |  |  |
| `sc_layer_batch_threshold_fullsort` | 80 |  |  |
| `sc_list_extradata_allocations` | *command* |  | Prints out the overall extra data allocation counts |
| `sc_max_framebuffer_copies_per_layer` | 1 |  |  |
| `sc_mesh_allow_batch_across_primitives` | true |  |  |
| `sc_mesh_backface_culling` | true |  |  |
| `sc_mesh_gpu_occlusion_culling` | true |  |  |
| `sc_mesh_gpu_volume_culling` | true |  |  |
| `sc_mesh_mesh_shaders` | false |  |  |
| `sc_mesh_shadows_batch_across_materials` | true |  |  |
| `sc_no_cull` | false |  |  |
| `sc_no_vis` | false |  |  |
| `sc_shadow_depth_bias` | 256 |  |  |
| `sc_shadow_depth_bias_clamp` | 0 |  |  |
| `sc_shadow_depth_bias_state_override` | false |  |  |
| `sc_shadow_slopescale_depth_bias` | 2.13 |  |  |
| `sc_spew_cmt_usage` | false |  |  |
| `sc_throw_away_all_layers` | false |  |  |
| `sc_use_clear_subrect` | false |  |  |
| `sc_view_profiler_frame_averaging` | 10 |  |  |
| `sc_visualize_batches` | 0 |  | color per batch |
| `sc_visualize_sceneobjects` | SCENEOBJECT_VIS_NONE | menubar_item | SceneSystem/Visualize SceneObject Mode |
| `scene_clientflex` | true | sv, rep | Do client side flex animation. |
| `scene_print` | 0 | sv, rep | When playing back a scene, print timing and event info to console. |
| `screenmessage_notifytime` | 8 | sv | How long to display screen message text |
| `screenshot` | *command* |  | Take a screenshot: screenshot [filename] |
| `screenshot_height` | -1 |  | Screenshot height. -1 for screen height. |
| `screenshot_prefix` | shot |  | Set the screenshot auto naming prefix. |
| `screenshot_subdir` | screenshots |  | Set the screenshot directory. |
| `screenshot_width` | -1 |  | Screenshot width. -1 for screen width. |
| `script_attach_debugger_at_startup` | false | sv |  |
| `script_break_in_native_debugger_on_error` | false | sv |  |
| `script_help2` | *command* | sv | Output help for script functions suitable for auto-completion |
| `scrubber` | *command* |  | Scrub system off - not a dev build |
| `server_game_time` | *command* | sv | Gives the game time in seconds (server's curtime) |
| `sk_player_arm` | 1 | sv |  |
| `sk_player_chest` | 1 | sv |  |
| `sk_player_head` | 2 | sv |  |
| `sk_player_leg` | 1 | sv |  |
| `sk_player_stomach` | 1 | sv |  |
| `skel_debug` | 0 | sv, rep |  |
| `slope_drop_enable` | true | sv, rep | Toggles a test dropping the view offset based on the slope |
| `slope_drop_max_offset` | 16 | sv, rep | The maximum distance to adjust the view height |
| `slope_drop_off_ground_blend_speed` | 160 | sv, rep | The speed with which the slope drop is blended out when the entity leaves the ground |
| `smoke_param1` | 6.26 | sv, rep |  |
| `smoke_param2` | 8.27 | sv, rep |  |
| `smoke_param3` | 0.13 | sv, rep |  |
| `smoke_param4` | 0 | sv, rep |  |
| `smoke_param5` | 0 | sv, rep |  |
| `smoke_use_noise_texture` | true | sv, rep |  |
| `smoothstairs` | true | sv, rep | Smooth player eye z coordinate when traversing stairs. |
| `snd_async_flush` | *command* |  | Flush all unlocked async audio data |
| `snd_async_showmem` | *command* |  | Show async memory stats |
| `snd_async_showmem_music` | *command* |  | Show async memory stats for just non-streamed music |
| `snd_async_showmem_summary` | *command* |  | Show brief async memory stats |
| `snd_async_spew_blocking` | 0 |  | Spew message to console any time async sound loading blocks on file i/o. |
| `snd_boxverb_simd` | true |  | Enable SIMD code path for shoebox reverb processor. |
| `snd_boxverb_simd_svf` | 1 |  | 0 = use biquad instead of svf, 1 = use vectorized svf, 2 = use scalar svf |
| `snd_compare_KV_convert` | false |  |  |
| `snd_delay_sound_ms_max` | 40 |  | Sound device synchronization max delay (ms) |
| `snd_delay_sound_ms_shift` | 23 |  | Sound device synchronization shift (ms) |
| `snd_diffusor_simd` | false |  | Enable SIMD code path for diffusor processor. |
| `snd_disable_radar_visualize` | false | sv, rep |  |
| `snd_enable_subgraph_corenull_passthrough` | true |  |  |
| `snd_enable_subgraph_log` | false |  |  |
| `snd_front_headphone_position` | *command* |  | Specifies the position (in degrees) of the virtual front left/right headphones. |
| `snd_front_stereo_speaker_position` | *command* |  | Specifies the position (in degrees) of the virtual front left/right speakers. |
| `snd_front_surround_speaker_position` | *command* |  | Specifies the position (in degrees) of the virtual front left/right speakers. |
| `snd_headphone_pan_exponent` | *command* |  | Specifies the exponent for the pan xfade from phone to phone if the 'exp' pan law is being used. |
| `snd_headphone_pan_radial_weight` | *command* |  | Apply cos(angle) * weight before pan law |
| `snd_hrtf_distance_behind` | 50 |  | HRTF calculations will calculate the player as being this far behind the camera. |
| `snd_max_pitch_shift_inaccuracy` | 0.08 | sv, rep |  |
| `snd_mergemethod` | 1 |  | Sound merge method (0 == sum and clip, 1 == max, 2 == avg). |
| `snd_opvar_set_dome_catchup_distance` | 64 | sv, rep |  |
| `snd_opvar_set_dome_catchup_rate` | 1 | sv, rep |  |
| `snd_opvar_set_dome_churn_fraction` | 0.25 | sv, rep |  |
| `snd_opvar_set_dome_cluster_steps_per_think` | 32 | sv, rep |  |
| `snd_opvar_set_point_update_interval` | 0.2 | sv, rep |  |
| `snd_opvar_set_point_update_interval_fast` | 0.0333 | sv, rep |  |
| `snd_print_current_mixer_mixgroup` | *command* |  | Get data related to mix group matching string |
| `snd_rear_headphone_position` | *command* |  | Specifies the position  (in degrees) of the virtual rear left/right headphones. |
| `snd_rear_stereo_speaker_position` | *command* |  | Specifies the position (in degrees) of the virtual rear left/right speakers. |
| `snd_rear_surround_speaker_position` | *command* |  | Specifies the position (in degrees) of the virtual rear left/right speakers. |
| `snd_side_surround_speaker_position` | *command* |  | Specifies the position (in degrees) of the virtual rear left/right speakers. |
| `snd_sos_beatpattern_show_operator_updates` | false |  |  |
| `snd_sos_debug_trigger_opvar` | false | sv |  |
| `snd_sos_hide_simple_parameter_overwrite_warnings` | true |  |  |
| `snd_sos_max_event_base_depth` | 4 |  |  |
| `snd_sos_report_entity_deleted` | false |  |  |
| `snd_sos_show_entry_match_free` | false |  |  |
| `snd_sos_show_mixgroup_path_errors` | false |  |  |
| `snd_sos_show_parameter_overwrite_value_comparisons` | false |  |  |
| `snd_sos_show_parameter_overwrite_warnings` | false |  |  |
| `snd_sos_show_soundevent_overwrites` | false |  |  |
| `snd_sos_show_track_list` | false |  |  |
| `snd_sos_show_voice_elapsed_time` | false |  |  |
| `snd_sos_soundevent_deferred_interval_time` | 0.1 |  |  |
| `snd_sos_soundevent_max_deferred_time` | 5 |  |  |
| `snd_sos_soundevent_show_deferral_warning` | false |  |  |
| `snd_sos_sv_soundevent_pause_last` | *command* | sv | Test |
| `snd_sos_sv_soundevent_start` | *command* | sv | Test |
| `snd_sos_sv_soundevent_stop_last` | *command* | sv | Test |
| `snd_sos_sv_soundevent_unpause_last` | *command* | sv | Test |
| `snd_sos_sv_test_gender` | *command* | sv | Test |
| `snd_soundmixer` | Default_Mix |  |  |
| `snd_soundmixer_flush` | *command* |  | Reload soundmixers.txt file. |
| `snd_soundmixer_list_mix_groups` | *command* |  | List all mix groups to dev console. |
| `snd_soundmixer_list_mix_layers` | *command* |  | List all mix layers to dev console. |
| `snd_soundmixer_list_mixers` | *command* |  | List all mixers to dev console. |
| `snd_soundmixer_version` | 2 |  |  |
| `snd_steamaudio_display_dimension_data_inside` | true |  | When visualizing dimensions data at runtime, draw the inside direction. |
| `snd_steamaudio_display_dimension_data_outside` | true |  | When visualizing dimensions data at runtime, draw the outisde direction. |
| `snd_steamaudio_display_dimension_data_size` | true |  | When visualizing dimensions data at runtime, draw the size of the space. |
| `snd_steamaudio_display_probes` | *command* |  | Load all the probes from a file and display probes based on the passed on arguments. |
| `snd_steamaudio_dynamicpathing_max_samples` | 16 | sv, rep |  |
| `snd_steamaudio_pathing_caching_threshold` | 5 | sv, rep |  |
| `snd_steamaudio_pathing_enable_caching` | true | sv, rep |  |
| `snd_steamaudio_source_pathing_debug_duration` | 0.01 |  | Duration for which path remains visible. Should be close to update rate of the sound operator stack. |
| `snd_steamaudio_source_pathing_enable_validation` | false |  | Enable real-time pathing validation against dynamic geometry. |
| `snd_stereo_speaker_pan_exponent` | *command* |  | Specifies the exponent for the pan xfade from speaker to speaker if the 'exp' pan law is being used. |
| `snd_stereo_speaker_pan_radial_weight` | *command* |  | Apply cos(angle) * weight before pan law |
| `snd_surround_speaker_pan_exponent` | *command* |  | Specifies the exponent for the pan xfade from speaker to speaker if the 'exp' pan law is being used. |
| `snd_surround_speaker_pan_radial_weight` | *command* |  | Apply cos(angle) * weight before pan law |
| `sndplaydelay` | *command* |  |  |
| `sos_debug_emit` | false | sv, rep |  |
| `sos_use_guid_filter` | false | sv, rep |  |
| `soundlist` | *command* |  | List all known sounds. |
| `soundpatch_captionlength` | 2 | sv, rep | How long looping soundpatch captions should display for. |
| `soundscape_flush` | *command* | sv | Flushes the server & client side soundscapes |
| `soundsystem_device_used` | 0 |  | Sound device in use (changing this does not change the soundsystem). |
| `soundsystem_update_async` | true |  |  |
| `soundsysteminfo` | *command* |  | Describe the current sound device without an active voice list. |
| `spawngroup_ignore_timeouts` | false |  |  |
| `spec_replay_fullframe` | true |  | Send full frame on every hltv replay transition |
| `spew_fonts` | *command* |  | Spew information about font manager fonts |
| `splitscreen_testreadconfigconflict` | *command* |  |  |
| `ss_add` | *command* |  | Adds a splitscreen user. |
| `ss_remove` | *command* |  | Removes a splitscreen user. |
| `ss_voice_hearpartner` | false |  | Route voice between splitscreen players on same system. |
| `start_rec_mic` | *command* | linked | Start recording to a desired wav. |
| `startmovie` | *command* | norecord | Start recording movie frames. |
| `stats` | *command* |  | Prints server performance variables |
| `stats_collect_gpu` | false |  | While doing stats_display, collect GPU perf counters. Used for stats_print_gpu. |
| `stats_display` | 0 |  | Displays perf statistics information |
| `stats_print` | *command* |  | Prints out perf statistics to the console, clears perf history |
| `stats_print_gpu` | *command* |  | Prints out GPU perf statistics to the console.  Requires stats_display > 0, and stats_collect_gpu = true.  Optional argument of CSV filename |
| `stop_rec_mic` | *command* | linked | Stop recording to a desired wav. |
| `stop_rec_mic_all` | *command* | linked | Stop recording all mic streams. |
| `sv_autosave` | true | sv, rep | Set to 1 to autosave game on level transition. Does not affect autosave triggers. |
| `sv_bot_parallel_threat_detection` | true | sv | Perform bot threat detection in parallel |
| `sv_c4_upright_constraint_damping` | 0.5 | sv | Controls how much velocity is damped on the constraint. 0 = undamped wobbly spring, 1 = critically damped no wobble fast converge, >1 = over damped |
| `sv_c4_upright_constraint_enabled` | true | sv | Use a constraint to keep C4 pointed upright when thrown |
| `sv_c4_upright_constraint_strength` | 0.6 | sv | How quickly the constraint converges |
| `sv_client_max_interp_ratio` | 5 | sv, rep | This can be used to limit the value of cl_interp_ratio for connected clients (only while they are connected). |
| `sv_client_min_interp_ratio` | 0 | sv, rep | This can be used to limit the value of cl_interp_ratio for connected clients (only while they are connected). |
| `sv_clientrates` | *command* |  | Show client rates. |
| `sv_clip_penetration_traces_to_players` | true | sv, rep |  |
| `sv_condense_late_buttons` | true | sv | When condensing late commands. Should we compress multiple moves of button presses into the target move? |
| `sv_cq_min_queue` | 0 | rep | Server min buffer size. |
| `sv_cs_dump_econ_item_stringtable` | *command* | sv | sv_cs_dump_econ_item_stringtable |
| `sv_debug_player_use` | 0 | sv, rep | Visualizes +use logic. Green cross=trace success, Red cross=trace too far, Green box=radius success |
| `sv_dev_entitydeltapadding_extra_max` | 0 |  | When encoding entity deltas, append on a random number of extra bytes.  This happens after sv_dev_entitydeltapadding_min_size. |
| `sv_dev_entitydeltapadding_extra_min` | 0 |  | When encoding entity deltas, append on a random number of extra bytes.  This happens after sv_dev_entitydeltapadding_min_size. |
| `sv_dev_entitydeltapadding_min_size` | 0 |  | When encoding entity deltas, if the delta size is < N bytes, then shove in N dummy bytes.  This happens before sv_dev_entitydeltapadding_extra_min/sv_dev_entitydeltapadding_extra_max |
| `sv_dev_simulate_gcdown` | *command* | sv | <state> Turn on/off simulated GC communications failure (GC is down in a way that we know it is down) |
| `sv_disable_reliable_delta_retransmit` | true |  | Assume that a reliable entity delta will be ack'ed and send future deltas relative to the last reliable delta. |
| `sv_extra_client_connect_time` | 15 |  | Seconds after client connect during which extra frames are buffered to prevent non-delta'd update |
| `sv_filterban` | 1 |  | Set packet filtering by IP mode |
| `sv_fullupdate` | *command* |  | Force a full update for all clients. |
| `sv_game_mode_convars` | *command* | sv | Display the values of the convars for the current game_mode. |
| `sv_histogram` | *command* |  | var change info histogram |
| `sv_hitbox_debug` | false | sv |  |
| `sv_ladder_angle` | -0.707 | sv, rep | Cos of angle of incidence to ladder perpendicular for applying ladder_dampen |
| `sv_ladder_dampen` | 0.2 | sv, rep | Amount to dampen perpendicular movement on a ladder |
| `sv_long_frame_ms` | 15 |  | If a server frame takes longer than N ms, complain about it.  (Dedicated server only.)  See also engine_frametime_warnings_enable. |
| `sv_massreport` | false | sv |  |
| `sv_matchperfstats_maxclientperfsamples` | 100 | sv | Don't retain more than N perf samples for any given client |
| `sv_max_distance_transmit_footsteps` | 1250 | sv, rep | Maximum distance to transmit footstep sound effects. |
| `sv_max_unreliable_delta_size` | 4096 |  | Maximum allowable entity delta size over unreliable delivery. |
| `sv_maxclientframes` | 128 |  |  |
| `sv_maxreplay` | 0 |  | Maximum replay time in seconds |
| `sv_mover_maxslope` | 0.7 | sv, nf, rep | The maximum slope the player can overcome [-] |
| `sv_mover_pogodampingratio` | 1 | sv, nf, rep | The capsule pogo stick damping ratio [-] |
| `sv_mover_pogofrequency` | 10 | sv, nf, rep | The capsule pogo stick frequency [hz]. |
| `sv_mute_players_with_social_penalties` | true | sv |  |
| `sv_nomvp` | false | sv | Disable MVP awards. |
| `sv_nonemesis` | true | sv | Disable nemesis and revenge. |
| `sv_nowinpanel` | false | sv | Turn on/off win panel on server |
| `sv_phys_animated_hierarchy` | true | sv |  |
| `sv_phys_async_buoyancy_update` | false | sv, rep | If true, server buoyancy motion controllers are updated in an async job after the tick has completed. |
| `sv_phys_visualize_awake` | false | sv |  |
| `sv_player_search_range` | 64 | sv, rep |  |
| `sv_pvs_entity` | -1 | sv | If set, only allows this ent index to network (other than players and things that force sending). |
| `sv_pvs_random` | false | sv | If set, objects blink in/out of pvs randomly. |
| `sv_querycache_stats` | *command* | sv | Display status of the query cache (client only) |
| `sv_rcon_banpenalty` | 0 |  | Number of minutes to ban users who fail rcon authentication |
| `sv_rcon_log` | true |  | Enable/disable rcon logging. |
| `sv_rcon_maxfailures` | 10 |  | Max number of times a user can fail rcon authentication before being banned |
| `sv_rcon_minfailures` | 5 |  | Number of times a user can fail rcon authentication in sv_rcon_minfailuretime before being banned |
| `sv_rcon_minfailuretime` | 30 |  | Number of seconds to track failed rcon authentications |
| `sv_recvbuf_messages` | 500 |  | Max number of messages that can be queued in a netchan receive buffer for an ordinary connection from a client. |
| `sv_regeneration_wait_time` | 1 | sv, rep |  |
| `sv_remapper_loopsoundfix` | false | sv, rep |  |
| `sv_remapper_range_multiplier` | 1 | sv, rep |  |
| `sv_replaysdir` | replays |  | Directory to store replays in |
| `sv_reserve_slots_for_reconnecting_players_kick_prior` | true |  | Kick a previously connected player with the same steamID if a replacement comes along |
| `sv_runcmds` | true | sv |  |
| `sv_script_think_interval` | 0.1 | sv, rep |  |
| `sv_sequence_debug` | -1 | sv |  |
| `sv_sequence_debug2` | -1 | sv |  |
| `sv_sequence_model_substring` | 0 | sv |  |
| `sv_shared_team_pvs` | false | sv | PVS is shared between teams |
| `sv_show_bot_difficulty_in_name` | false | sv, rep | 0 = hide bot difficulty in bot name, 1 = show bot difficulty in bot name |
| `sv_showladders` | false | sv | Show bbox and dismount points for all ladders (must be set before level load.) |
| `sv_showplayerhitboxes` | 0 | sv, rep | Show lag compensated hitboxes for the specified player index whenever a player fires. |
| `sv_showtags` | *command* |  | Describe current gametags. |
| `sv_shutdown_immediately_on_request` | false |  | The server will always shutdown on receiving the shutdown request, even if not hibernating |
| `sv_sniper_tracer_mode` | 1 | sv, rep | Mode for sniper tracers. 0: legacy, 1: hide when more than sv_sniper_tracer_innacuracy inaccurate. |
| `sv_stats` | true |  | Collect CPU usage stats |
| `sv_strict_notarget` | false | sv | If set, notarget will cause entities to never think they are in the pvs |
| `sv_temp_baseline_string_table_buffer_size` | 524288 |  | Buffer size for writing string table baselines |
| `sv_timeout` | 20 |  | After this many seconds without a message from fully connected client, the client is dropped |
| `sv_turbophysics` | false | sv, rep | Turns on turbo physics |
| `sv_usenetworkvars` | true |  | Use networkvar system. |
| `sv_vote_issue_changelevel_allowed` | true | sv | Can people hold votes to change levels? |
| `sv_vote_issue_matchready_allowed` | true | sv | Can people hold votes to ready/unready the match? |
| `sv_vote_issue_nextlevel_allowed` | true | sv | Can people hold votes to set the next level? |
| `sv_vote_issue_nextlevel_allowextend` | true | sv | Allow players to extend the current map? |
| `sv_vote_issue_nextlevel_choicesmode` | true | sv | Present players with a list of lowest playtime maps to choose from? |
| `sv_vote_issue_nextlevel_prevent_change` | true | sv | Not allowed to vote for a nextlevel if one has already been set. |
| `sv_vote_issue_pause_match_allowed` | true | sv | Can people hold votes to pause/unpause the match? |
| `sv_vote_issue_scramble_teams_allowed` | false | sv | Can people hold votes to scramble the teams? |
| `sv_vote_issue_surrrender_allowed` | true | sv | Can people hold votes to surrender? |
| `sv_vote_issue_swap_teams_allowed` | false | sv | Can people hold votes to swap the teams? |
| `sv_vote_issue_timeout_allowed` | true | sv | Can people hold votes to time out? |
| `sys_minidumpexpandedspew` | true |  |  |
| `target_scan_use_query_cache` | true | sv |  |
| `test_voice_container_nesting` | *command* | linked | Test nesting voice containers. |
| `test_voice_containers` | *command* | linked | Quick example for how we'd derive traits from voice containers. |
| `testscript_debug` | false |  | Debug test scripts. |
| `throttle_expensive_ai` | false | sv |  |
| `traceattack` | *command* | sv | traceattack damage hitgroup |
| `tv_allow_camera_man` | true | sv | Auto director allows spectators to become camera man |
| `tv_broadcast_resend` | *command* |  | resend broadcast data to broadcast relay |
| `tv_demo_starttick` | 0 |  |  |
| `tv_extended_logging` | false |  |  |
| `tv_grouprelaydatareliable` | false |  | When enabled, this will collect all information for relay sending into a single datagram to ensure that the data stays together through a potentially large number of relays |
| `tv_grouprelaydataunreliable` | false |  | When enabled, this will collect all information for relay sending into a single datagram to ensure that the data stays together through a potentially large number of relays |
| `tv_grouprelaydatavoice` | false |  | Similar to tv_grouprelaydata, but controls whether or not the voice channels should be routed into the grouped data for the relays |
| `tv_instant_replay_full_frame` | true |  | Send embedded full frames |
| `tv_instant_replay_full_frame_build_threaded` | false |  | Build the full frames on a seperate job thread |
| `tv_instant_replay_full_frame_time` | 30 |  | Seconds between full frame embeddeds |
| `tv_log_director_events` | false | sv | Log game events being considered by the director |
| `tv_msg` | *command* | sv | Send a screen message to all clients. |
| `tv_rate_multiplier` | 2 |  | Multiply requested rate by this value to adjust Dota TV send rate |
| `tv_relay_hard_shutdown` | false |  |  |
| `tv_relay_quit_after_game` | true |  | Quit after a game has been relayed, do not hibernate |
| `tv_relay_rate` | 500000 |  | default rate for relays |
| `tv_relay_secret_code` | false |  | When enabled, this will use a uniquely generated server code to authenticate relay to relay connections. This code is coordinated via the GC or some external means rather than by clients directly |
| `tv_secret_code` | false |  | When enabled, this will use a uniquely generated server code to authenticate relay connections. This code is coordinated via the GC or some external means rather than by clients directly |
| `tv_threaded_merge_entity_deltas` | true |  | Enable SourceTV threading of delta merging |
| `tv_update_hibernation_enabled` | false |  | Allow SourceTV to control server hibernation state. |
| `update_voices_low_priority` | false |  |  |
| `users` | *command* |  | Show user info for players on server. |
| `vis_debug_currentcluster` | *command* |  | Show the current cluster number |
| `vis_debug_drawcluster` | *command* |  | Add cluster # to visualization, (-1) to clear |
| `vis_debug_dumpvisibleclusters` | *command* |  | Show the list of visible clusters |
| `vis_debug_find_los` | *command* |  | Find or clear the vis LOS to here |
| `vis_debug_lock` | *command* |  | Lock vis LOS origin to current |
| `vis_debug_record_start` | *command* |  | Record a path to debug vis |
| `vis_debug_record_stop` | *command* |  | Record a path to debug vis |
| `vis_debug_show` | *command* |  | Show/hide the vis debug visualization |
| `vis_debug_sunclusters` | *command* |  | Showing clusters for sun/csm rendering. Red (full sun csm & lighting), Orange (no viewmodel sun or csm), Green (no sun at all) |
| `vis_debug_tracelos` | *command* |  | Trace rays and check vis from the current camera |
| `vis_enable` | true |  | Enable precomputed visibility when true |
| `vmem_dump` | *command* |  | Dump memory stats to log. |
| `vmix_debug_list` | *command* |  | Debug dump the list of available vmix graphs |
| `voice_containers_get_instance_args` | *command* | linked | Args: [Voice Container Path] |
| `voice_containers_get_instance_params` | *command* | linked | Args: [Voice Container Path] |
| `voice_debugfeedbackfrom` | false |  |  |
| `voice_fadeouttime` | 0.005 |  |  |
| `voice_in_process` | true |  |  |
| `voice_initial_buffer_ms` | 200 |  |  |
| `voice_min_buffer_ms` | 100 |  |  |
| `voice_noise_supression` | false |  |  |
| `voice_sequence_maximum_wait_time` | 0.5 |  | When receiving packets out of sequence, wait this many seconds for missing sequences to arrive |
| `voice_serverdebug` | false | sv |  |
| `voice_stall_ms` | 250 |  |  |
| `volume_fog_depth` | 128 |  | Depth of volume fog texture |
| `volume_fog_depth_warp` | 7 |  |  |
| `volume_fog_depth_warp_debug` | false |  |  |
| `volume_fog_height` | 160 |  | Height of volume fog texture |
| `volume_fog_intermediate_textures_hdr` | true |  |  |
| `volume_fog_shadow_penumbra_multiplier` | 3 |  | Penumbra size multiplier for shadow sampling, reduces fog shadow aliasing |
| `volume_fog_temporal_filter` | true |  |  |
| `volume_fog_temporal_weight` | 0.9 |  | Temporal filtering weight |
| `volume_fog_width` | 240 |  | Width of volume fog texture |
| `vprof_counters` | 0 |  |  |
| `vprof_counters_show_minmax` | false |  |  |
| `vprof_dump_counters` | *command* |  | Dump vprof counters to the console |
| `vprof_generate_report` | *command* |  | Generate a report to the console. |
| `vprof_generate_report_budget` | *command* |  | Generate a report to the console based on budget group. |
| `vprof_generate_report_hierarchy` | *command* |  | Generate a report to the console. |
| `vprof_off` | *command* |  | Disable vprof |
| `vprof_on` | *command* |  | Enable vprof |
| `vprof_remote_start` | *command* |  | Request a VProf data stream from the remote server (requires authentication) |
| `vprof_remote_stop` | *command* |  | Stop an existing remote VProf data request |
| `vprof_reset` | *command* |  | Reset the stats in VProf profiler |
| `vprof_reset_peaks` | *command* |  | Reset just the peak time in VProf profiler |
| `vprof_scope_entity_thinks` | false | sv, rep |  |
| `vprof_think_limit` | false | sv |  |
| `vt_sim_streaming_delay_ms` | 500 |  |  |
| `vtune` | *command* |  | Controls VTune's sampling. |
| `weapon_molotov_maxdetonateslope` | 30 | sv, rep | Maximum angle of slope on which the molotov will detonate |
| `wind_system_default_resolution_xy` | 256 |  |  |
| `wind_system_default_resolution_z` | 32 |  |  |
| `wind_system_default_sample_min_spacing` | 12 |  |  |
| `wind_system_temporal_smoothing` | true |  |  |
| `workshop_clear_cloud_save` | *command* | sv | Remove a workshop save from steam cloud. Pass the published file id to delete or 0 to delete the non-workshop addon save. |
| `workshop_dump_cloud_contents` | *command* | sv | Spew contents of steam cloud. |
| `world_dump_loaded_worlds` | *command* |  | Dump all of the worlds that we know about |
| `world_layer_list` | *command* |  | List all world layers |
| `world_layer_set_visible` | *command* |  | Show or hide the specified world layer |
| `writeid` | *command* |  | Writes a list of permanently-banned user IDs to file. |
| `writeip` | *command* |  | Save the ban list to file. |
